# enrollment/cli.py
import click
from enrollment.database import init_db, engine
from enrollment.models import Base, Student, Course, Enrollment

# Ensure tables exist
init_db()

@click.group()
def cli():
    """Student Course Enrollment CLI"""
    pass

@cli.command()
@click.option("--name", prompt="Student name")
@click.option("--email", prompt="Student email")
def add_student(name, email):
    from sqlalchemy.orm import Session
    db = Session(bind=engine)
    new_student = Student(name=name, email=email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    click.echo(f"✅ Student {name} added.")

@cli.command()
@click.option("--title", prompt="Course title")
@click.option("--description", prompt="Course description")
def add_course(title, description):
    from sqlalchemy.orm import Session
    db = Session(bind=engine)
    new_course = Course(title=title, description=description)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    click.echo(f"✅ Course '{title}' added.")

@cli.command()
@click.option("--student_email", prompt="Student email")
@click.option("--course_title", prompt="Course title")
def enroll(student_email, course_title):
    from sqlalchemy.orm import Session
    db = Session(bind=engine)
    student = db.query(Student).filter_by(email=student_email).first()
    course = db.query(Course).filter_by(title=course_title).first()
    if student and course:
        enrollment = Enrollment(student_id=student.id, course_id=course.id)
        db.add(enrollment)
        db.commit()
        click.echo(f"{student.name} enrolled in {course.title}")
    else:
        click.echo("Student or Course not found.")

@cli.command()
@click.option("--student_email", prompt="Student email")
def view_courses(student_email):
    from sqlalchemy.orm import Session
    db = Session(bind=engine)
    student = db.query(Student).filter_by(email=student_email).first()
    if student:
        for e in student.enrollments:
            click.echo(f"- {e.course.title}: {e.course.description}")
    else:
        click.echo("Student not found.")

if __name__ == "__main__":
    cli()