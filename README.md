<h1>UFlow</h1>
<h4>University of Alabama Computer Science Capstone Project (CS 495)</h4>
<h4>Group: Cassidy Baumann, Mikey McDavid, Peyton Reed, Brady Wachs</h4>
<br>

<h2>How to use the UFlow web application</h2>
<p>
  Go to the 
  <a href='https://uflow-alabama.herokuapp.com'>UFlow project home page.</a> <br>
  Create an account, filling out all required fields on the registration page. <br>
  A user will be taken to the <code>/logged_in</code> page. <br>
  From here a user can edit any of the given flowcharts by clicking on the edit button. This takes them to the <code>/flowchart</code> page. <br>
  Currently, you can choose the <code>taken</code>, <code>in progress</code>, or <code>future</code> buttons. Once you select a button, you can click all classes associated with this status. <br>
  &emsp;- A user can toggle between these statuses at anytime. <br>
  A user can save their flowcharts from this page. The flowchart will be saved to the database before opening a new, unedited flowchart. <br>
</p>
<br>

<h2>How to run the UFlow application on a local machine</h2>
<p>
  Clone project repository to your local machine. <br>
  &emsp;- One way to clone: <code>git clone https://github.com/cmbaumann/uflow.git</code> <br>
  Navigate to the <code>uflow</code> directory. <br>
  Use the command <code>python run.py</code> to run the application. <br>
  Click on the provided hyperlink in your terminal to view the application from a local host. <br>
  The terminal output should look something like: <br>
  <pre>
    <code>
   * Serving Flask app 'sourcecode.app' (lazy loading) <br>
   * Environment: production <br>
     WARNING: This is a development server. Do not use it in a production deployment. <br>
     Use a production WSGI server instead. <br>
   * Debug mode: off <br>
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) <br>
    </code>
  </pre>
</p>
