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
<style>
  .bmi-calculator {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.bmi-calculator h2 {
    margin-bottom: 20px;
}

.bmi-calculator label {
    display: block;
    margin-bottom: 10px;
}

.bmi-calculator input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.bmi-calculator button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    background-color: #28a745;
    color: #fff;
    cursor: pointer;
}

.bmi-calculator button:hover {
    background-color: #218838;
}

#result {
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
}

  

/* Responsive Design */
@media (max-width: 600px) {
    .bmi-calculator {
        padding: 15px;
    }
    
    .bmi-calculator h2 {
        font-size: 20px;
    }
    
    .bmi-calculator input {
        width: 100%;
        padding: 8px;
        font-size: 16px;
    }
    
    .bmi-calculator button {
        padding: 8px 16px;
        font-size: 14px;
    }
    
    #result {
        font-size: 16px;
    }
}

  .contact-us {
    background-color: #696e71;
    color: #fff;
    padding: 80px 0;
}

.contact-info {
    padding-right: 50px; /* Adjust spacing */
}

.heading-contact {
    font-size: 36px;
    font-weight: 700;
    color: rgb(57, 255, 123);
    margin-bottom: 30px;
    position: relative;
}

.heading-contact::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -10px;
    background-color: rgb(57, 255, 123);
    width: 60px;
    height: 4px;
}

.para-contact {
    font-size: 18px;
    font-weight: 500;
    line-height: 28px;
    margin-bottom: 30px;
}

.contact-list {
    list-style: none;
    padding: 0;
}

.contact-list li {
    margin-bottom: 20px;
    position: relative;
    padding-left: 30px;
    font-size: 16px;
    line-height: 28px;
}

.contact-list li i {
    position: absolute;
    left: 0;
    top: 2px;
    font-size: 20px;
    color: rgb(57, 255, 123);
}

.contact-form {
    background-color: #696e71;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 20px #787c7f;
}

.drop{
    background-color: #787c7f;
    color: #fff;
}
.dd{
     background-color: #787c7f;
}

.contact-form .form-group {
    margin-bottom: 20px;
}

.contact-form input[type="text"],
.contact-form input[type="email"],
.contact-form textarea {
    background-color: rgba(255, 255, 255, 0.1);
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 12px;
    width: 100%;
    font-size: 16px;
    transition: background-color 0.3s ease;
}

.contact-form textarea {
    resize: none;
    height: 120px;
}

.contact-form textarea:focus,
.contact-form textarea:active {
    background-color: rgba(255, 255, 255, 0.5); 
}

.contact-form input::placeholder,
.contact-form textarea::placeholder {
    color: #fff; /* Placeholder text color */
}

.btn-contact {
    background-color: rgb(57, 255, 123);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 600;
    text-transform: uppercase;
    transition: background-color 0.3s ease;
}

.btn-contact:hover {
    background-color: transparent;
}
.btn-send-message {
    display: inline-block;
    padding: 10px 43px;
    border: 1px solid rgb(57, 255, 123);
    color: white;
    border-radius: 50px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    background-color: rgb(57, 255, 123);
    transition: background-color 0.2s, color 0.2s, border-color 0.2s;
}

.btn-send-message:hover {
    background-color: transparent;
    color: #E1E2E4;
    border-color: rgb(57, 255, 123);
}

      .num-contact{
            text-decoration: none;
            color: #a7a7a7;
        }

</style>
    
    <title>BMI Calculator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
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
                    <a class="nav-link" aria-current="page" href="./index.py">Home</a>
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
    </div>
<div class="container">
    <div class="bmi-calculator">
        <h2>BMI Calculator</h2>
        <form id="bmiForm">
            <label for="weight">Weight (kg):</label>
            <input type="number" id="weight" name="weight" required>
            <label for="height">Height (cm):</label>
            <input type="number" id="height" name="height" required>
            <button type="button" onclick="calculateBMI()">Calculate BMI</button>
        </form>
        <div id="result"></div>
    </div>
</div>
    <script src="scripts.js"></script>
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