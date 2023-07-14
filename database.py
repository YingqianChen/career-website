from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://xs1w3qvpv6r26iag34rv:pscale_pw_bAMp8VCOg0ijrDRfwJnJQDn832tvYfsnP8BSCwB9tLA@aws.connect.psdb.cloud/quantum_innovations_careers?charset=utf8mb4'

engine = create_engine(
  db_connection_string,
  connect_args={
    'ssl': {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_job(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :id"), {'id': id})
    job = result.all()
    if len(job) == 0:
      return None
    else:
      return job[0]._asdict()


def add_application(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                  {'job_id':job_id, 
                  'full_name':data['full_name'],
                  'email':data['email'],
                  'linkedin_url':data['linkedin_url'],
                  'education':data['education'],
                  'work_experience':data['work_experience'],
                  'resume_url':data['resume_url']})
