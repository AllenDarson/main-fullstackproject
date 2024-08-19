#!C:/Users/USER/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src='https://kit.fontawesome.com/4c729db828.js' crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js" integrity="sha512-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="media.css">
    <style>
      .num-contact{
            text-decoration: none;
            color: #a7a7a7;
        }
    </style>
    <title>RED MUSCLE GYM</title>
  </head>
<body>
    <div class="header">
        <div class="container-fluid gx-0">
            <!--navbar start--> 
            <nav class="navbar navbar-expand-lg">
                <div class="container">
                  <a class="navbar-brand logo text-uppercase" href="./index.py">The Red Muscle Gym</a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                      <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="index.py">Home</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="./aboutus.py">About Us</a>
                      </li>
                      <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown"  data-bs-toggle="dropdown" aria-expanded="false">
                            Services
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="./calisthenics.py">Calisthenics</a></li>
                            <li><a class="dropdown-item" href="./weight.py">Weight Loss & Weight Gain</a></li>
                            <li><a class="dropdown-item" href="./bodybuilding.py">Bodybuilding</a></li>
                            <li><a class="dropdown-item" href="./powerlifting.py">Powerlifting</a></li>
                            <li><a class="dropdown-item" href="./sports-specific.py">Sport-Specific Training</a></li>
                            <li><a class="dropdown-item" href="./zumba.py">Zumba Dance Training</a></li>
                        </ul>
                    </li>
                      <li class="nav-item">
                        <a class="nav-link" href="./locations.py">Location</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="./nutrition.py">Nurtition</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="./bmi.py">BMI Calculator</a>
                      </li>
                      <li class="nav-item">
                        <a class="btn-navbar" href="#contact-us">Join Now</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </nav>
            <!--navbar end-->
            <div class="container">
              <div class="content-home">
                  <div class="row content-home2">
                      <div class="col-lg-7 col-md-5">
                          <div class="box-container">
                              <img src="./weightlifter-3944725_1920.png" class="img-home" alt="banner img">
                          </div>
                      </div>
                      <div class="col-lg-5 col-md-7">
                          <div class="box-container2">
                              <h1 class="home-heading"><span class="home-span">Power Lifting</span></h1>
                              </div>
                      </div>    
                  </div>
              </div>
          </div>

          
        
          <div class="container" id="aboutus">
            <div class="Nutrition">
                <div class="health-us">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="content-about" style="background-color: transparent;">
                                <h2 class="heading-about">Powerlifting</h2>
                                <p>
                                    1.Squat:The lifter must lower their body until the hip crease is below the top of the knee and then stand back up.This lift primarily targets the quadriceps, hamstrings, glutes, and lower back.
                                  </p> 
                                <p>
                                    2.Bench Press:The lifter lies on a bench and lowers the barbell to the chest, then presses it back up to arm's length.This lift mainly works the pectorals, triceps, and shoulders.
                                  </p>
                                <p >
                                    3.Deadlift:The lifter lifts the barbell from the ground to a standing position, with hips and knees locked out.This lift engages the entire posterior chain, including the hamstrings, glutes, and lower back.
                                  </p>
                                  <h2 class="heading-about">Equipment</h2>
                                <p >
                                    1.Belt: Provides core stability and support for the lower back.
                                    <br>
                                    2.Wrist Wraps: Protects the wrists and improves grip strength.
                                    <br>
                                    3.Specialized Shoes: Enhances stability and reduces stress on the knees and ankles.
                                    <br>
                                    4.Knee Sleeves/Wraps: Offer knee support and warmth.
                                        </p>            
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
<!--contact us page-->
<!-- Contact Us Section -->
<section class="contact-us" id="contact-us">
  <div class="container">
    <div class="row">
      <!-- Contact Info Section -->
      <div class="col-lg-6">
        <div class="contact-info">
          <h2 class="heading-contact">STAY IN TOUCH</h2>
          <p class="para-contact">
            We are here to answer any questions you may have about our products. Reach out to us and we'll respond as soon as we can.
          </p>
          <ul class="contact-list">
            <li><i class="fas fa-map-marker-alt"></i> Umapathi Towers - 72 Lakshmipuram, 6th Street, Masakalipalayam Rd, Peelamedu, Coimbatore, Tamil Nadu 641004</li>
            <li><i class="fas fa-phone-alt"></i><a href="tel:+918760961525" class="num-contact"> Phone: +91 8760961525</a></li>
            <li><i class="fas fa-envelope"></i><a href="mailto:allendarson27@gmail.com" class="num-contact"> Email: servicesector.redmusclegym@gmail.com</a></li>
          </ul>
        </div>
      </div>
 <div class="col-lg-6">
              <form class="contact-form">
                  <div class="form-group">
                      <input type="text" class="form-control" placeholder="Your Name" name="name" required>
                  </div>
                  <div class="form-group">
                      <input type="email" class="form-control" placeholder="Your Email" name="mail" required>
                  </div>
                  <div class="form-group">
                      <label for="Services" class="service">Services</label>
                      <select class="dd" id="Services" name="services" required>
                          <optgroup label="Class" class="drop">
                              <option value=""></option>
                              <option value="Strength Training">Strength Training</option>
                              <option value="Weight Loss & Weight Gain">Weight Loss & Weight Gain</option>
                              <option value="Calisthenics">Calisthenics</option>
                              <option value="Body Building">Body Building</option>
                              <option value="Powerlifting">Powerlifting</option>
                              <option value="Sports-specific Training">Sports-specific Training</option>
                              <option value="Zumba Dance Training">Zumba Dance Training</option>
                          </optgroup>
                      </select>
                  </div>
                  <div class="form-group">
                      <textarea class="form-control" rows="5" placeholder="Your Message" name="msg" required></textarea>
                  </div>
                    <input type="submit" name="submit" class="btn btn-info">
              </form>""")
import smtplib
import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="gym")
cur = conn.cursor()

form = cgi.FieldStorage()

pid = form.getvalue("id")
pname = form.getvalue("name")
pemailid = form.getvalue("mail")
pservices = form.getvalue("services")
pmessage = form.getvalue("msg")
psubmit = form.getvalue("submit")

if psubmit != None:
    q = """insert into enquire(Name,Email,Services,Message) values('%s','%s','%s','%s')""" % (
    pname, pemailid, pservices, pmessage)
    cur.execute(q)
    conn.commit()

    fromaddr = "allendarson27@gmail.com"
    password = "ebbg qhms qvcr xuuk"
    toaddr = pemailid
    subject = "Hi,We Heard You"
    body = """ Username: '%s' \n mailid: '%s' \n Service: '%s' \n Yes you heard it right , We heard your request from you , and we like to assist you further and unfortunately our team is not active now , we will surely call you back """ % (
    pname, pemailid, pservices)
    msg = """ Subject:{}\n\n{}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print("""
        <script>
            alert("Thank You for your Registration");
        </script>
    """)

conn.close()
print("""</div>
      </div>
  </div>
</section>
<!--foooter-->
<footer class="footer">
  <div class="container">
      <div class="footer-content">
          <div class="footer-about">
              <h3 class="footer-logo">The Red Muscle GYM</h3>
              <p>Strength.Dedication.Power</p>
          </div>
          <ul class="footer-links">
              <li><a href="#">Home</a></li>
              <li><a href="./aboutus.py">About Us</a></li>
              <li><a href="./bmi.py">BMI Calculator</a></li>

          </ul>
          <div class="footer-social">
              <a href="https://www.facebook.com/"><i class="fab fa-facebook-f"></i></a>
              <a href="https://x.com/?lang=en"><i class="fab fa-twitter"></i></a>
              <a href="https://www.instagram.com/"><i class="fab fa-instagram"></i></a>
          </div>
      </div>
      <div class="footer-bottom">
          <p>&copy; 2024 The Red Muscle Gym. All rights reserved. 
      </div>
  </div>
</footer>
  </body>
<!-- script file -->
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</html>""")