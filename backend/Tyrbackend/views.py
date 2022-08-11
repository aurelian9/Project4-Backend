from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/view', methods=['GET'])
@login_required
def home2():
    return render_template('home.html', user=current_user)


@views.route('/view/<note_id>', methods=['GET'])
@login_required
def view(note_id):
    noteId = note_id
    note = Note.query.filter_by(id=noteId).first()
    if note == noteId:
        flash("Viewing entry.", category="success")
    return render_template('testview.html', user=current_user)
    
    
@views.route('/record', methods=['GET', 'POST'])
@login_required
def record():
    if request.method == 'POST':
        man_date = request.form.get('manual_date')
        bod_part = request.form.get('body_parts')
        note = request.form.get('note')
        ex_name = request.form.get('exercise_name')
        sets = request.form.get('num_of_sets')
        reps = request.form.get('num_of_reps')
        
        if len(note) < 1:
            flash("Note is too short!", category="error")
        elif len(bod_part) < 4: 
            flash("Please enter a valid body part", category="error")
        elif len(ex_name) < 4:
            flash("Please enter a valid exercise", category="error")
        elif sets.isnumeric() == False:
            flash("Please enter a valid number.", category="error")
        elif reps.isnumeric() == False:
            flash("Please enter a valid number", category="error")
        else:
            new_note = Note(
                manual_date = man_date, 
                body_parts = bod_part, 
                exercise_name = ex_name, 
                num_of_sets = sets, 
                num_of_reps = reps, 
                data = note, 
                user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Workout Recorded!", category="success")
            
    return render_template("record.html", user=current_user)


@views.route('/edit', methods=['GET'])
@login_required
def send():
    return render_template("data.html", user=current_user)


@views.route('/edit/<note_id>', methods=['GET', 'POST'])
@login_required
def edit(note_id):
    noteId = note_id
    note = Note.query.filter_by(id=noteId).first()
    if request.method == 'POST':
        note.manual_date = request.form.get('manual_date')
        note.body_parts = request.form.get('body_parts')
        note.data = request.form.get('note')
        note.exercise_name = request.form.get('exercise_name')
        note.num_of_sets = request.form.get('num_of_sets')
        note.num_of_reps = request.form.get('num_of_reps')
        
        if len(note.data) < 1:
            flash("Note is too short!", category="error")
        elif len(note.body_parts) < 4: 
            flash("Please enter a valid body part", category="error")
        elif len(note.exercise_name) < 4:
            flash("Please enter a valid exercise", category="error")
        elif note.num_of_sets == 0:
            flash("You did nothing?", category="error")
        elif note.num_of_sets.isnumeric() == False:
            flash("Please enter a valid number.", category="error")
        elif note.num_of_reps == 0:
            flash("You did nothing?", category="error")
        elif note.num_of_reps.isnumeric() == False:
            flash("Please enter a valid number.", category="error")
        else:
            db.session.commit()
            flash("Workout updated!", category="success")
    
    return render_template("data.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note: 
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})