from flask import Flask, render_template, request, jsonify, Response
import random
import datetime
import sys


app = Flask(__name__)

images = [
 "https://i2.wp.com/www.libraryforsmartinvestors.com/wp-content/uploads/2017/02/aws_logo.jpg?fit=500%2C500&ssl=1",
 "http://australiaday.openstack.org.au/wp-content/uploads/2016/01/openstack_500x500.png",
 "http://isoc.ae/image/cache/catalog/courses/Google%20Cloud%20Compute%20Engine%20Essential%20Training-500x500.jpg",
 "https://static.onthehub.com/production/attachments/9/9cb7d193-f0b7-e611-9423-b8ca3a5db7a1/7d04d71c-c4e0-4df8-8e07-ff33bf12915e.png",
 "https://aptira.com/wp-content/uploads/2016/09/kubernetes_logo.png",
 "https://www.opsview.com/sites/default/files/docker.png"
]

reference_date = datetime.datetime(2020, 4, 27, 1, 0, 0)

def date_greater_or_equal(arg_date, ref_date):
 if arg_date.year != ref_date.year:
  return (arg_date.year - ref_date.year > 0)
 if arg_date.month != ref_date.month:
  return (arg_date.month - ref_date.month > 0)
 if arg_date.day != ref_date.day:
  return (arg_date.day - ref_date.day > 0)
 
 if arg_date.hour != ref_date.hour:
  return (arg_date.hour - ref_date.hour > 0)
 if arg_date.minute != ref_date.minute:
  return (arg_date.minute - ref_date.minute > 0)
 if arg_date.second != ref_date.second:
  return (arg_date.second - ref_date.second > 0)
 
 return True

@app.route('/')
def indexx():
 url = random.choice(images)
 return render_template('index.html', url=url, vol_name="volume nameee")

@app.route('/button_pressed')
def index():
 _now = datetime.datetime.now() + datetime.timedelta(hours=3)
 if date_greater_or_equal(_now, reference_date):
  return render_template('index_post.html', email="email is: hearthstone1bogdanut@gmail.com", password_email="password (of the email) is: #", password_blizzard="password (of blizzard account) is: #", my_str_date=str(_now), announcing_date=str(reference_date))
 else:
  return render_template('index_post.html', email="email is: To be announced", password_email="password (of the email) is: To be announced", password_blizzard="password (of blizzard account) is: To be announced", my_str_date=str(_now), announcing_date=str(reference_date))

if __name__ == "__main__":
 app.run(host="0.0.0.0")
