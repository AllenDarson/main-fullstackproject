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
                  <a class="nav-link" aria-current="page" href="./index.py">Home</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="./aboutus.py">About Us</a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown" aria-expanded="false">
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
                  <a class="nav-link" href="./nutrition.py">Nutrition</a>
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
        <div class="container">
          <div class="content-home">
              <div class="row content-home2">
                  <div class="col-lg-7 col-md-5">
                      <div class="box-container">
                          <img src="./silhouette-3839252_1920.png" class="img-home" alt="banner img">
                      </div>
                  </div>
                  <div class="col-lg-5 col-md-7">
                      <div class="box-container2">
                          <h1 class="home-heading"><span class="home-span">Calisthenics</span></h1>
                          </div>
                  </div>    
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
                          <h2 class="heading-about">Calisthenics</h2>
                          <p >
                             Calisthenics is a form of exercise that uses body weight for resistance training. It focuses on movements such as push-ups, pull-ups, squats, and planks to build strength, flexibility, and endurance. Calisthenics workouts can be performed anywhere without the need for equipment, making them accessible and versatile. This form of exercise improves overall fitness by targeting multiple muscle groups simultaneously, promoting functional strength and agility. Calisthenics routines can be tailored to suit different fitness levels, from beginners to advanced athletes, by adjusting intensity and variations of exercises. It emphasizes body control, balance, and core stability, making it a popular choice for those seeking a holistic approach to fitness and strength training.
                              </p> 
                          <h2 class="heading-about">Key Components</h2>
                          <p >
                               1. Bodyweight Exercises: Calisthenics relies primarily on bodyweight exercises, making it accessible and convenient.<br>
            2. Basic Movements: Core movements include push-ups, pull-ups, squats, dips, and lunges.<br>
            3. Progressive Overload: To build strength and muscle, gradually increasing the difficulty of exercises is essential.<br>
            4. Full-Body Workout: Calisthenics engages multiple muscle groups simultaneously, promoting overall strength and coordination.
                              <br>
                              <h2 class="heading-about">Benefits</h2>    
                              1. Builds Strength and Endurance: Consistent practice improves muscular strength and cardiovascular endurance.<br>
            2. Flexibility and Mobility: Many exercises enhance joint mobility and muscle flexibility.<br>
            3. Core Stability: Emphasizes core strength, leading to better posture and balance.<br>
            4. Minimal Equipment: Only a bar or similar structure is needed for pull-ups and dips, reducing costs and space requirements.
                              <h2 class="heading-about">Training Structure</h2>   
                          
                             1. Warm-Up: Dynamic stretches and light cardio to prepare muscles and joints.<br>
            2. Skill Work: Practicing specific movements like handstands or muscle-ups.<br>
            3. Strength Training: Focused sets and repetitions of basic exercises.<br>
            4. Cool-Down: Stretching and mobility work to aid recovery.
                              <h2 class="heading-about">Popular Exercise</h2>
                               1. Push-Ups: Targets chest, shoulders, and triceps.<br>
            2. Pull-Ups: Engages back, biceps, and forearms.<br>
            3. Squats: Strengthens quadriceps, hamstrings, and glutes.<br>
            4. Dips: Works triceps, chest, and shoulders.<br>
            5. Lunges: Improves leg strength and balance.<br>
            6. Planks: Builds core stability and strength.<br>
            7. Muscle-Ups: Combination of a pull-up and a dip.<br>
            8. Human Flag: Demonstrates powerful core and shoulder strength.
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>

    <!--TESTIMONIALS-->
    <section class="testimonial">
      <h2 class="heading-testimonial">
        What Our Customers Think <span class="styling">About Us</span>
      </h2>
      <p class="para-testimonial">At Red Muscle Unisex Fitness Center, we take pride in the positive feedback and testimonials we receive from our valued members. Here's what some of our customers have to say about their experience with us:</p>
      <div class="container-fluid">
        <div id="carouselExampleIndicators" class="carousel slide">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          </div>
          <div class="carousel-inner">
            <!-- Slide 1 -->
            <div class="carousel-item active">
              <div class="container container-clients">
                <div class="row">
                  <div class="col-lg-4 col-md-6 my-2">
                    <div class="container-content">
                      <div class="img-client"></div>
                      <div class="star">
                        <ul class="rating">
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                      <p class="para-client">"Red Muscle Gym transformed my fitness journey."</p>
                      <h2 class="name-client">Karthibakrishnan</h2>
                      <p class="para-client">"Red Muscle has transformed my fitness journey. The facilities are top-notch, and the trainers are incredibly supportive. I've never felt more motivated to reach my goals."</p>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 my-2">
                    <div class="container-content">
                      <div class="img-client"></div>
                      <div class="star">
                        <ul class="rating">
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                      <p class="para-client">"Exceptional trainers and facilities!"</p>
                      <h2 class="name-client">Aadhityan</h2>
                      <p class="para-client">"A gym with good ambience. Staffs are very friendly and giving good support for all clients. General training is very good especially my trainer Robin is supporting very well. Thank you so much"</p>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 my-2">
                    <div class="container-content">
                      <div class="img-client"></div>
                      <div class="star">
                        <ul class="rating">
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                      <p class="para-client">"A welcoming community for all fitness levels."</p>
                      <h2 class="name-client">Sakthivel</h2>
                      <p class="para-client">"Neat and clean gym spacious and hygienic. Very comfortable for women. Highly recommended. Trainers are helpful and friendly in nature."</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- Slide 2 -->
            <div class="carousel-item">
              <div class="container container-clients">
                <div class="row">
                  <div class="col-lg-4 col-md-6 my-2">
                    <div class="container-content">
                      <div class="img-client"></div>
                      <div class="star">
                        <ul class="rating">
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                      <p class="para-client">"Top-notch equipment and clean environment."</p>
                      <h2 class="name-client">Vignesh</h2>
                      <p class="para-client">"Gym ambience is very good and neatly maintained traines are well knowledge it’s one of the peaceful place to workout without distractions."</p>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 my-2">
                    <div class="container-content">
                      <div class="img-client"></div>
                      <div class="star">
                        <ul class="rating">
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                      <p class="para-client">"Personalized training programs that deliver results."</p>
                      <h2 class="name-client">Joseph</h2>
                      <p class="para-client">"I have been a member for 1 year I have seen a big amount of difference. They have very good trainers who guided me very well"</p>
                    </div>
                  </div>
                  <div class="col-lg-4 col-md-6 my-2">
                    <div class="container-content">
                      <div class="img-client"></div>
                      <div class="star">
                        <ul class="rating">
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                          <li class="stars"><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                      <p class="para-client">"Motivating and encouraging trainers."</p>
                      <h2 class="name-client">sanjay</h2>
                      <p class="para-client">"Wonderful gym, great environment for workouts. The trainers are encouraging, supportive and knowledgeable. Awesome place to start our fitness journeys."</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </section>
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