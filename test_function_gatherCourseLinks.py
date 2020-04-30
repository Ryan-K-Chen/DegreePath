import requests
from bs4 import BeautifulSoup
from csv import writer

html_doc = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!-- saved from url=(0014)about:internet -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<link rel="stylesheet" href="./Catalog Entries_files/web_defaultapp.css" type="text/css">
<link rel="stylesheet" href="./Catalog Entries_files/web_defaultprint.css" type="text/css" media="print">
<title>Catalog Entries</title>
<meta http-equiv="Content-Script-Type" name="Default_Script_Language" content="text/javascript">
<script language="JavaScript" type="text/javascript">
<!-- Hide JavaScript from older browsers 
window.onunload = function() {submitcount=0;}
var submitcount=0;
function checkSubmit() {
if (submitcount == 0)
   {
   submitcount++;
   return true;
   }
else
   {
alert("Your changes have already been submitted.");
   return false;
   }
}
//  End script hiding -->
</script>
<script language="JavaScript" type="text/javascript">
<!-- Hide JavaScript from older browsers 
//  Function to open a window
function windowOpen(window_url) {
   helpWin = window.open(window_url,'','toolbar=yes,status=no,scrollbars=yes,menubar=yes,resizable=yes,directories=no,location=no,width=350,height=400');
   if (document.images) { 
       if (helpWin) helpWin.focus()
   }
}
//  End script hiding -->
</script>
</head>
<body>
<div class="headerwrapperdiv">
<div class="pageheaderdiv1">
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_display_courses#main_content" onmouseover="window.status=&#39;Go to Main Content&#39;; return true" onmouseout="window.status=&#39;&#39;; return true" onfocus="window.status=&#39;Go to Main Content&#39;; return true" onblur="window.status=&#39;&#39;; return true" class="skiplinks">Go to Main Content</a>
<h1> Georgia Tech</h1></div><div class="headerlinksdiv">
</div>
<table class="plaintable" summary="This table displays Menu Items and Banner Search textbox." width="100%">
<tbody><tr>
<td class="pldefault">
<div class="headerlinksdiv2">
&nbsp;
</div>
</td>
<td class="pldefault"><p class="rightaligntext" p="">
<span class="pageheaderlinks">
<a href="https://oscar.gatech.edu/wtlhelp/twbhhelp.htm" accesskey="H" onclick="popup = window.open(&#39;/wtlhelp/twbhhelp.htm&#39;, &#39;PopupPage&#39;,&#39;height=500,width=450,scrollbars=yes,resizable=yes&#39;); return false" target="_blank" onmouseover="window.status=&#39;&#39;;  return true" onmouseout="window.status=&#39;&#39;; return true" onfocus="window.status=&#39;&#39;;  return true" onblur="window.status=&#39;&#39;; return true" class="submenulinktext2">HELP</a>
|
<a href="https://oscar.gatech.edu/pls/bprod/twbkwbis.P_Logout" accesskey="3" class="submenulinktext2">EXIT</a>
</span>
</p></td>
</tr>
</tbody></table>
</div>
<div class="pagetitlediv">
<table class="plaintable" summary="This table displays title and static header displays." width="100%">
<tbody><tr>
<td class="pldefault">
<h2>Catalog Entries</h2>
</td>
<td class="pldefault">
&nbsp;
</td>
<td class="pldefault"><p class="rightaligntext" p="">
</p><div class="staticheaders">
Fall 2020<br>
Mar 22, 2020<br>
</div>
</td>
</tr>
<tr>
<td class="bg3" width="100%" colspan="3"><img src="./Catalog Entries_files/web_transparent.gif" alt="Transparent Image" class="headerImg" title="Transparent Image" name="web_transparent" hspace="0" vspace="0" border="0" height="3" width="10"></td>
</tr>
</tbody></table>
<a name="main_content"></a>
</div>
<div class="pagebodydiv">
<!--  ** END OF twbkwbis.P_OpenDoc **  -->
<div class="infotextdiv"><table class="infotexttable" summary="This layout table contains information that may be helpful in understanding the content and functionality of this page.  It could be a brief set of instructions, a description of error messages, or other special information."><tbody><tr><td class="indefault"><img src="./Catalog Entries_files/web_info_cascade.png" alt="Information" class="headerImg" title="Information" name="web_info" hspace="0" vspace="0" border="0" height="12" width="14"></td><td class="indefault"><span class="infotext"> <b>The pre-requisites listed in this catalog are those approved by the Curriculum Committee.
<br>For pre-requisite information specific to an individual instance of a course, please see the schedule of classes.<br><b>Click the Schedule Type to find available offerings of the course on the Schedule of Classes.</b></b></span></td></tr></tbody></table><p></p></div>
<table class="datadisplaytable" summary="This table lists all course detail for the selected term." width="100%">
<tbody><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3005">ECE 3005 - ECE Prof/Tech Comm</a></td>
</tr>
<tr>
<td class="ntdefault">
Written, oral, and visual communication skills required by electrical and computer engineers.  Prepares students for advanced communication tasks required in academic and professional settings.
<br>
    1.000 Credit hours
<br>
    2.000   Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3005&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3006">ECE 3006 - ECE Co-Curric Prof Comm</a></td>
</tr>
<tr>
<td class="ntdefault">
This course documents student completion of ECE professional communications requirement through workshops, seminars, research projects, co/extra-curricular activities, etc.
<br>
    0.000 Credit hours
<br>
    0.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>A 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3006&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3020">ECE 3020 - Math Foundations of CmpE</a></td>
</tr>
<tr>
<td class="ntdefault">
Fundamental concepts in discrete mathematics and their efficient realization via algorithms, data structures, computer programs, and hardware.  Discussion of engineering and computational applications.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3020&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3025">ECE 3025 - Electromagnetics</a></td>
</tr>
<tr>
<td class="ntdefault">
To present the laws and applications of electromagnetics.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3025&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3030">ECE 3030 - Physical Foundations CmpE</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic principles governing the physical realization of computing systems and their relationship to characteristics such as performance, energy, and robustness.  Implementation technologies.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3030&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3035">ECE 3035 - Mechanisms-Computing Sys</a></td>
</tr>
<tr>
<td class="ntdefault">
Computing system execution and storage mechanisms, starting with instruction set architecture and concluding with support for high level languages and operating systems.  Credit not allowed for both ECE 3035 and ECE 2035.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3040">ECE 3040 - Microelectronic Circuits</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic concepts of microelectronic materials, devices, and circuits.
<br>
    4.000 Credit hours
<br>
    4.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3040&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3041">ECE 3041 - Instrument&amp; Circuits Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Fundamental experimental techniques for the laboratory analysis of signals and passive electrical circuits using basic electronic test and measurement instrumentation. Component characterization, computer-automated measurements, and simulation. Technical writing.  Credit not allowed for both ECE 3041 and ECE 3043.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3042">ECE 3042 - Microelectro Circuit Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Design, analysis, simulation, implementation, and evaluation of electronic circuits. Employs op amp, clock, counter, and converter integrated circuits, discrete diodes, bipolar junction, and field effect transistors; and some integrated circuits.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3043">ECE 3043 - Circuits&amp;Electronics Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic electronic test instrumentation.  Elementary passive and active circuits using both discrete (diodes, bipolar junction transistors, MOSFETs) and integrated devices (operational amplifiers).  Credit not allowed for both ECE 3043 and ECE 3041.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3043&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3050">ECE 3050 - Analog Electronics</a></td>
</tr>
<tr>
<td class="ntdefault">
To present concepts of analysis and design of electronic circuits and systems. Biasing, small-signal analysis, frequency response, feedback amplifiers, active filters, non-linear op-amp applications, and oscillators.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3055">ECE 3055 - Computer Arch &amp; Oper Sys</a></td>
</tr>
<tr>
<td class="ntdefault">
Core concepts of computer architecture and operating systems.  Instruction set architectures (ISA), compiler/ISA relationships, pipelined datapaths. Memory hierarchy, memory management, and protection. Processes, threads, CPU scheduling, and associated techniques.  Credit not allowed for both ECE 3055 and ECE 3056.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3057">ECE 3057 - Arch, Sys, Conc &amp; Engy Comp</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic organizational principles of the major components of a processor - the core, memory hierarchy, I/O subsystem and basic operating system constructs that utilize them.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3057&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3060">ECE 3060 - VLSI &amp; Adv Digital Dsgn</a></td>
</tr>
<tr>
<td class="ntdefault">
Advanced digital design issues in the context of VLSI systems.  Introduction to a design methodology that encompasses the range from behavioral models to circuit simulation. Credit will not be awarded for ECE 3060 and ECE 3150.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3065">ECE 3065 - Electromagnetic Apps</a></td>
</tr>
<tr>
<td class="ntdefault">
To present concepts in waveguiding and radiation, with application to microwaves, antennas, and optics. Credit will not be awarded for ECE 3065 and ECE 4350.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3070">ECE 3070 - Elec Energy Conversion</a></td>
</tr>
<tr>
<td class="ntdefault">
This course serves as an introduction to three-phase power systems, electromechanical energy conversion, and operating principles of electric machines.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3071">ECE 3071 - Electric Energy Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
Non-renewable and renewable/sustainable energy sources. Processes, costs, and environmental impact of conversion into electric energy.  Delivery and control of electric energy, electromechanical systems.  Credit not allowed for both ECE 3071 and ECE 3072.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3072">ECE 3072 - Elec Energy Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
Non-renewable and renewable/sustainable energy sources.  Processes, costs, and environmental impact of conversion into electric energy.  Delivery and control of electric energy, electromechanical systems.  Credit not allowed for both ECE 3072 and ECE 3071.

<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
    0.000 OR     2.000 Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3072&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3075">ECE 3075 - Random Signals</a></td>
</tr>
<tr>
<td class="ntdefault">
Study of random variables and random processes for applications in electrical and computer engineering. Includes an introduction to statistical filtering, parameter estimation, Markov processes.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3076">ECE 3076 - Computer Communications</a></td>
</tr>
<tr>
<td class="ntdefault">
Presents the basic concepts of computer communications network protocols.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3077">ECE 3077 - Prob/Stats for ECE</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to probability, random variables, distributions, estimation, confidence intervals, linear regression and other tools for describing and managing uncertainty in electrical and computer engineering.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3077&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3080">ECE 3080 - Semiconductor Devices</a></td>
</tr>
<tr>
<td class="ntdefault">
To gain an understanding of the device needs for current and future computers, and fiber optic and wireless communication systems addressing the future needs of high- frequency, GHz-range, device operation.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3084">ECE 3084 - Signals and Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
Continuous-time linear systems and signals, their mathematical representations, and computational tools.  Fourier and Laplace transforms, convolutions, input-output responses, stability.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3084&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3085">ECE 3085 - Intro Systems &amp; Control</a></td>
</tr>
<tr>
<td class="ntdefault">
Theory of linear time-invariant systems for continuous and discrete time. Laplace and Z-Transforms. Transfer function and state space representations. Introduction to feedback control theory.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3090">ECE 3090 - Software for Engr System</a></td>
</tr>
<tr>
<td class="ntdefault">
Using computer algorithms for solving electrical engineering problems arising in various application domains.  Development of effective algorithms and their implementation by object-oriented code.  Credit not allowed for both ECE 3090 and ECE 2036.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3150">ECE 3150 - VLSI &amp; Adv Digital Dsgn</a></td>
</tr>
<tr>
<td class="ntdefault">
Advanced digital design issues in the context of VLSI systems. Introduction to a design methodolgy that encompasses the range from architectural models to circuit simulation. Credit not awarded for ECE 3150 and ECE 3060.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3300">ECE 3300 - Elec Energy Conversion</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to three phase power systems, electromechanical energy conversion and operating principles of electric machines.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3300&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3400">ECE 3400 - Analog Electronics</a></td>
</tr>
<tr>
<td class="ntdefault">
Analysis and design of electronic circuits and systems.  Biasing, small-signal analysis, frequency response, feedback amplifiers, active filters, non-linear op-amp applications, and oscillators.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3400&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3431">ECE 3431 - Analog Electronics Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Design, analysis, simulation, implementation, and evaluation of advanced electronic circuits.   Employs bipolar junction, metal oxide semiconductor and field effect transistors; and some integrated circuits.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3450">ECE 3450 - Semiconductor Devices</a></td>
</tr>
<tr>
<td class="ntdefault">
Properties of semiconductor devices.  Applications in current and future computers, fiber optic and wireless communication systems.  Future needs of high frequency, GHz-range, device operation.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3450&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3550">ECE 3550 - Feedback Control Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
Analysis and design of control systems.  Laplace transforms, transfer functions, and stability.  Feedback systems: tracking and disturbance rejection.  Graphical design techniques.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3550&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3600">ECE 3600 - Computer Communications</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic concepts of computer communication network protocols.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3600&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3710">ECE 3710 - Circuits &amp; Electronics</a></td>
</tr>
<tr>
<td class="ntdefault">
An introduction to electric circuit elements and electronic devices and a study of circuits containing such devices.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3710&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3741">ECE 3741 - Instrum &amp; Electronic Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic analog and digital electronic circuits and principles. Techniques of electrical and electronic measurements with laboratory instruments.
<br>
    1.000 Credit hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3741&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3801">ECE 3801 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    1.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3802">ECE 3802 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    2.000 Credit hours
<br>
    2.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3803">ECE 3803 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3804">ECE 3804 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    4.000 Credit hours
<br>
    4.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3805">ECE 3805 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    5.000 Credit hours
<br>
    5.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3811">ECE 3811 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    1.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3812">ECE 3812 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    2.000 Credit hours
<br>
    2.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3813">ECE 3813 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3814">ECE 3814 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    4.000 Credit hours
<br>
    4.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3815">ECE 3815 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    5.000 Credit hours
<br>
    5.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3872">ECE 3872 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     2.000 Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3872&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3881">ECE 3881 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    0.000   Lecture hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3882">ECE 3882 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3883">ECE 3883 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3884">ECE 3884 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3891">ECE 3891 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3892">ECE 3892 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3893">ECE 3893 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3894">ECE 3894 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3894&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3900">ECE 3900 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3901">ECE 3901 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3901&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3902">ECE 3902 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3902&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3903">ECE 3903 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3903&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3951">ECE 3951 - Undergrad Research I</a></td>
</tr>
<tr>
<td class="ntdefault">
Participation in an individual or group research project under the direction of a faculty member.
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>P 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3951&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences, Res/CP  ≤ 30 cont hrs 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3952">ECE 3952 - Undergrad Research II</a></td>
</tr>
<tr>
<td class="ntdefault">
Participation in an individual or group research project under the direction of a faculty member. Requires a formal research report.
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>L 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=3952&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences, Res/CP 31-50 cont hrs 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=3XXX">ECE 3XXX - Elec/Comp Engr Elective</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>T 
<br>
Dept/Registrar Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4001">ECE 4001 - Engr Practice &amp; Profess</a></td>
</tr>
<tr>
<td class="ntdefault">
Technical tools and professional issues for engineering practice and early career development.  Engineering ethics, design tools, financial and economic principles, project management, probabilistic and statistical techniques, and decision making.  Credit not allowed for both ECE 4001 and ECE 4000.
<br>
    2.000 Credit hours
<br>
    2.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4007">ECE 4007 - ECE Design Project</a></td>
</tr>
<tr>
<td class="ntdefault">
Team-oriented culminating design project in electrical/ computer engineering, incorporating engineering standards and realistic constraints.  Requires formal reports and group presentations.  Credit not allowed for both ECE 4007 and ECE 4006.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     6.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4011">ECE 4011 - ECE Culminating Design 1</a></td>
</tr>
<tr>
<td class="ntdefault">
First semester of ECE culminating design sequence.  Design tools, financial principles, project management, probabilistic and statistical techniques, team forming.  Requires formal reports and group presentations.
<br>
    2.000 Credit hours
<br>
    2.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4011&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4012">ECE 4012 - ECE Culminating Design 2</a></td>
</tr>
<tr>
<td class="ntdefault">
Second semester of ECE culminating design sequence.  Team project in ECE incorporating engineering standards and realistic constraints.  Requires formal reports and group presentations.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     6.000 Lab hours
<br>
    0.000 OR     2.000 Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4012&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4043">ECE 4043 - Analog Electronics Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Experiments in analog electronics using discrete devices and off-the-shelf integrated circuits.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4043&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4100">ECE 4100 - Adv Computer Architecure</a></td>
</tr>
<tr>
<td class="ntdefault">
Comprehensive coverage of the architecture and system issues that confront the design of high-performance workstation/PC computer architectures with emphasis on quantitative evaluation. Credit is not allowed for both ECE 4100 and any of the following courses: ECE 6100, CS 4290, CS 6290.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4100&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4110">ECE 4110 - Internetwork Programming</a></td>
</tr>
<tr>
<td class="ntdefault">
Exploration of Internet implementation as a network of computing systems. Internetworking skills for design and implementation of hardware and software Internet products.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4112">ECE 4112 - Internetwork Security</a></td>
</tr>
<tr>
<td class="ntdefault">
Hands-on experimentation and evaluation of internet security theory, principles, and practices. Laboratory component involves implementing both defensive and offensive security techniques.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4115">ECE 4115 - Intro to Comp Security</a></td>
</tr>
<tr>
<td class="ntdefault">
Introductory topics in computer security are presented with an emphasis on fundamental security primitives and current security challenges facing society. Credit not awarded for both ECE 4115 and ECE 4112.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4115&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4122">ECE 4122 - Adv Prog Techniques</a></td>
</tr>
<tr>
<td class="ntdefault">
Course covers a number of programming techniques for distributed and parallel computing and other advanced methods, such as multiprecision arithmetic and nonblocking I/O. Credit not awarded for ECE 4122 and ECE 6122.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4122&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4130">ECE 4130 - Adv VLSI Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
An advanced treatment of VLSI systems analysis, design, and testing with emphasis on complex systems and how they are incorporated into a silicon environment. Credit is not allowed for both ECE 4130 and ECE 6130.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4130&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4147">ECE 4147 - Adv Malware Analysis</a></td>
</tr>
<tr>
<td class="ntdefault">
This course covers advanced approaches for the analysis of malicious software and explores recent research and unsolved problems in software protection and forensics.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4147&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4150">ECE 4150 - Cloud Computing</a></td>
</tr>
<tr>
<td class="ntdefault">
Cloud computing technologies, computation models, and applications, design methodologies for cloud applications, use of cloud-based languages and tools in developing advanced applications.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4170">ECE 4170 - HDL Based Design</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to hardware description languages and associated methodologies for digital system design. In-depth coverage includes applications to the simulation and synthesis of digital systems.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4175">ECE 4175 - Emb Microcontroller Dsgn</a></td>
</tr>
<tr>
<td class="ntdefault">
Microcontroller structure, instruction set, addressing modes. Code development by assembly language programming and using an emulator. Programmable timer use, interrupt handlers, and timing.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4180">ECE 4180 - Embedded Systems Design</a></td>
</tr>
<tr>
<td class="ntdefault">
Processors, chipsets, busses, and I/O devices for high-ended embedded systems. Embedded operating systems; device drivers and applications for embedded systems.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4180&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4181">ECE 4181 - Embedded Comp Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
Algorithms and methodologies for the design of real-time, low-power embedded computing systems.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4185">ECE 4185 - Emb Microcontroller Des</a></td>
</tr>
<tr>
<td class="ntdefault">
Design, implement, and debug embedded micro-controller systems.  Develop code; understand underlying assembly code instructions and addressing modes.  Use ADC, timers, and other resources.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4260">ECE 4260 - Random Signals &amp; Appl</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to random signals and processes with emphasis on applications in ECE.  Includes basic estimation theory, linear prediction, and statistical modeling.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4270">ECE 4270 - Fund-Digital Signal Proc</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to digital signal processing. Sampling theorem, discrete-time Fourier transform. Power spectrum, discrete Fourier transform and the FFT algorithm, Z-transform, digital filter design and implementation.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4270&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4271">ECE 4271 - Applications of DSP</a></td>
</tr>
<tr>
<td class="ntdefault">
Applications of DSP in speech, image processing, radar, pattern recognition, and adaptive filtering requiring working software implementations applied to the analysis of real signals.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4273">ECE 4273 - DSP Chip Design</a></td>
</tr>
<tr>
<td class="ntdefault">
Fundamentals of theory and practice of DSP chip design in VHDL. Exposure to tools and environments for chip design, simulation, and verification.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4320">ECE 4320 - Power Sys Analy&amp; Control</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduces basic concepts in electric power generation, distribution, system control, and economic operation.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4320&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4321">ECE 4321 - Power System Engineering</a></td>
</tr>
<tr>
<td class="ntdefault">
To introduce basic concepts of electric power system design, encompassing protection, stability, and control.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4325">ECE 4325 - Electric Power Quality</a></td>
</tr>
<tr>
<td class="ntdefault">
Transients and harmonics in power systems, analysis methods and mitigation practices.  Causes of power quality problems and relationship to equipment susceptibility.  Credit not allowed for both ECE 4325 and ECE 6340.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4330">ECE 4330 - Power Electronics</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduces power semiconductor devices and power electronic converters, including single-phase and three-phase ac/dc rectifiers, ac voltage controllers, dc/dc converters, and dc/ac inverters.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4330&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4335">ECE 4335 - Elec Machinery Analysis</a></td>
</tr>
<tr>
<td class="ntdefault">
Advanced theory of AC machines, including AC motor winding design, finite element analysis, induction motor design, permanent magnet machine design, and synchronous machine dynamics.  Credit is not allowed for both ECE 4335 and ECE 6335.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4350">ECE 4350 - Electromag Applications</a></td>
</tr>
<tr>
<td class="ntdefault">
Presents concepts of electromagnetic fields applied to microwave circuit design and antenna radiation. Credit will not be awarded for ECE 4350 and ECE 3065.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4350&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4360">ECE 4360 - RF-Microwave Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
RF/microwave measurement theory and techniques. Use of state-of-the-art equipment operating into the GHz range.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4370">ECE 4370 - Antenna Engineering</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic theory, application, and design of a broad range of antennas.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4370&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4371">ECE 4371 - Antenna Engineering Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Experimentation to develop a practical understanding of antennas and their properties.
<br>
    1.000 Credit hours
<br>
    0.000   Lecture hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4371&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4390">ECE 4390 - Radar and EM Sensing</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduces students to radar systems, including pulsed, CW, CWFM, and MTI radars. Other techniques for electromagnetic sensing such as radiometry and EM tagging are discussed.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4391">ECE 4391 - Electromag Compatibility</a></td>
</tr>
<tr>
<td class="ntdefault">
To study electromagnetic interference and susceptibility of electrical systems, with application to analog and digital circuits.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4410">ECE 4410 - Analog Filters</a></td>
</tr>
<tr>
<td class="ntdefault">
An introduction to the theory, design techniques, and applications of analog passive, active, and switched- capacitor filters.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4415">ECE 4415 - RF Engineering I</a></td>
</tr>
<tr>
<td class="ntdefault">
Fundamentals of RF engineering. Components at high frequencies, device modeling, amplifiers, lumped-element and microstrip impedance transformation networks, S-parameter-based design of RF and microwave amplifiers.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4415&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4418">ECE 4418 - RF Engineering II</a></td>
</tr>
<tr>
<td class="ntdefault">
Fundamentals learned in RF-I are employed to design the elements of radio receivers, transmitters, and similar systems.  Systems analysis, mixers, detectors, power amplifiers, low-noise amplifiers, and oscillators are covered.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4420">ECE 4420 - Digital Integ Circuits</a></td>
</tr>
<tr>
<td class="ntdefault">
Analysis and design of bipolar and MOS digital integrated circuit families and their applications in modern electronic systems.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4430">ECE 4430 - Analog Integra Circuits</a></td>
</tr>
<tr>
<td class="ntdefault">
Analysis and design of analog ICs using analytic techniques and CAD tools. Topics include amplifiers, current sources, output circuits, and other analog building blocks.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4430&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4435">ECE 4435 - Operational Amp Design</a></td>
</tr>
<tr>
<td class="ntdefault">
Analysis and design techniques for utilization of integrated circuit operational amplifiers for applications in electronic systems.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4445">ECE 4445 - Audio Engineering</a></td>
</tr>
<tr>
<td class="ntdefault">
Concepts of acoustics and electroacoustic modeling for the analysis and design of microphones, loudspeakers, and crossover networks. Methods of analysis and design of audio power amplifiers.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4445&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4446">ECE 4446 - Audio Engineering Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
A companion laboratory to ECE 4445. Design, analysis, construction, modeling, and testing of circuits and systems pertaining to audio engineering.
<br>
    1.000 Credit hours
<br>
    0.000   Lecture hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4446&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4450">ECE 4450 - Analog for Music Synth</a></td>
</tr>
<tr>
<td class="ntdefault">
Circuits from classic analog synthesizers: nonlinear waveshapers and voltage-controlled oscillators, filters, and amplifier using operational transconductance amplifliers and the dynamic resistance of semiconductors.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4451">ECE 4451 - Semiconductor Dev-Commun</a></td>
</tr>
<tr>
<td class="ntdefault">
Advanced development of semiconductor device theory focusing on optoelectronic emitters, detectors, and high- frequency transistors to provide an understanding of devices used in communications systems.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4452">ECE 4452 - IC Fabrication</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to microelectronic processing technologies and CMOS. Includes a laboratory for fabrication/testing of MOS transistors, basic CMOS circuits, integrated resistors and capacitors. Credit will not be awarded for ECE 4452 and ECE 4752.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4452&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4460">ECE 4460 - Electronic Packaging</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to packaging technologies, technology drivers, electrical performance, thermal management, materials, optoelectronics, RF integration, reliability, system issues, assembly, testing.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4470">ECE 4470 - Renewable Energy Devices</a></td>
</tr>
<tr>
<td class="ntdefault">
Students study the engineering compromises, operational physics and environmental impact of a variety of devices from solar cells, batteries, thermoelectric devices and wind generators.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4500">ECE 4500 - Optical Engineering</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to applications of geometric, physical optics to engineering, including optical measurements, matrix methods, instruments, interference, holography, beam optics, Fourier optics, and diffraction.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4500&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4501">ECE 4501 - Fiber Optics</a></td>
</tr>
<tr>
<td class="ntdefault">
Combined lecture-laboratory exploration of the technology of fiber optics, with special emphasis on optical fiber communications systems. Credit will not be awarded for ECE 4501 and ECE 4502.
<br>
    0.000 OR     5.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     4.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4502">ECE 4502 - Optical Fiber Comm</a></td>
</tr>
<tr>
<td class="ntdefault">
Combined lecture-laboratory exploration of the technology of fiber optics, with emphasis on optical fiber communication systems. Credit will not be awarded for ECE 4502 and ECE 4501.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4550">ECE 4550 - Control System Design</a></td>
</tr>
<tr>
<td class="ntdefault">
Design of control algorithms using state-space methods, microcontroller implementation of control algorithms, and laboratory projects emphasizing motion control applications.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4550&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4551">ECE 4551 - Systems &amp; Controls I</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduction to feedback control.  Root locus and bode design for SISO systems, continuous and discrete. Introduction to state space formulation, continuous and discrete.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4555">ECE 4555 - Embedded&amp;Hybrid Control</a></td>
</tr>
<tr>
<td class="ntdefault">
Modeling, analysis, and design of embedded and hybrid control systems.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4560">ECE 4560 - Intro-Automation&amp;Robotic</a></td>
</tr>
<tr>
<td class="ntdefault">
Concurrent engineering principles; robotic manipulator kinematics, dynamics, and control; applications of robots in industry, medicine, and other areas; team projects and hands-on laboratory experience.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4560&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4562">ECE 4562 - Neural Nets &amp; Fuzzy Ctrl</a></td>
</tr>
<tr>
<td class="ntdefault">
Principles of neural networks and fuzzy systems; the MATLAB Neural Network and Fuzzy Logic Toolboxes; examples from system identification, classification, and control; laboratory experience.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4563">ECE 4563 - Game Theory</a></td>
</tr>
<tr>
<td class="ntdefault">
An introduction to game theory and its application to multiagent systems, including distributed routing, multivehicle control, and networked systems.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4570">ECE 4570 - Modern System Theory</a></td>
</tr>
<tr>
<td class="ntdefault">
Study of the basic concepts in linear system theory and numerical linear algebra with applications to communication, computation, control, and signal processing. A unified treatment.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4570&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4575">ECE 4575 - Numerical Methods Optim</a></td>
</tr>
<tr>
<td class="ntdefault">
Algorithms for numerical optimization and optimal control, Gradient-descent techniques, linear programming, numerical linear system solvers, second-order methods of optimizing performance of dynamical systems.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4580">ECE 4580 - Computer Vision</a></td>
</tr>
<tr>
<td class="ntdefault">
Computational and theoretical aspects of computer vision. Application areas include robotics, autonomous vehicles, tracking, and image-guided surgery. Includes major project.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4601">ECE 4601 - Communication Systems</a></td>
</tr>
<tr>
<td class="ntdefault">
To present the fundamentals of modern digital communication systems and evaluate their performance with realistic channel models.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4602">ECE 4602 - Communication System Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
To examine the performance of analog and digital telecommunications systems and components. Credit will not be awarded for ECE 4612 and ECE 4602.
<br>
    1.000 Credit hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4604">ECE 4604 - Network Dsgn&amp;Simulation</a></td>
</tr>
<tr>
<td class="ntdefault">
Introduces the principles of Monte Carlo techniques and network simulation, and applies them to design issues in ATM systems.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4605">ECE 4605 - Topics in Networks</a></td>
</tr>
<tr>
<td class="ntdefault">
Reviews on networking fundamentals. Latest networking technologies in wireless and wireline networks. Machine learning and data science in networks or other emerging topics. Projects included.
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4606">ECE 4606 - Wireless Communications</a></td>
</tr>
<tr>
<td class="ntdefault">
Cellular concept, wireless propagation modeling; types of digital modulation used in wireless systems, diversity combining, performance over fading channels, and multiple access techniques.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4606&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4607">ECE 4607 - Mobile&amp;Wireless Networks</a></td>
</tr>
<tr>
<td class="ntdefault">
Basics of mobile and wireless networking. Architectures and communication protocols for wireless sensor networks, wireless local area networks, ad-hoc networks, cellular systems, WiMAX, and Wireless Mesh Networks.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4612">ECE 4612 - Telecom Systems Lab</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic digital telecommunications systems are examined in a laboratory setting using electronic modules, covering concepts such as modulation, channel coding, AWGN, eye diagrams, and BER. Credit will not be awarded for ECE 4612 and ECE 4602.
<br>
    1.000 Credit hours
<br>
    0.000   Lecture hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Capstone 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4698">ECE 4698 - Research Assistantship</a></td>
</tr>
<tr>
<td class="ntdefault">
Independent research conducted under the guidance of a faculty member.
<br>
    1.000 TO    12.000 Credit hours
<br>
    1.000 TO    12.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>A 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4698&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Res/CP 51-100 cont/hrs 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4699">ECE 4699 - Undergraduate Research</a></td>
</tr>
<tr>
<td class="ntdefault">
Independent Research conducted under the guidance of a faculty member.
<br>
    1.000 TO    12.000 Credit hours
<br>
    1.000 TO    12.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>LP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4699&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences, Res/CP 51-100 cont/hrs 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4751">ECE 4751 - Laser Theory&amp;Application</a></td>
</tr>
<tr>
<td class="ntdefault">
Provides an introduction to the theory and applications of laser principles and related instrumentation. Emphasis is on the fundamental principles underlying laser action. Crosslisted with PHYS 4751.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4752">ECE 4752 - IC Fabrication</a></td>
</tr>
<tr>
<td class="ntdefault">
Gives students exposure to the various steps involved in the fabrication of integrated circuits and devices.  The course will include a laboratory segment in which students fabricate MOS transistors, diffused resistors, and MOS capacitors from a bare silicon substrate. Crosslisted with CHE 4752. Credit will not be awarded for ECE 4752 and ECE 4452.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4753">ECE 4753 - Topics in Engr Practice</a></td>
</tr>
<tr>
<td class="ntdefault">
Topics of current importance offered in collaboration with an approved partner of Georgia Tech's Distance Learning Program. Crosslisted with ME 4753.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4754">ECE 4754 - Elec Packaging Assembly</a></td>
</tr>
<tr>
<td class="ntdefault">
The course provides hands-on instruction in electronics packaging, including assembly, reliability, thermal management, and test of next-generation microsystems.  Crosslisted with ME and MSE 4754.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     6.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4755">ECE 4755 - Packaging Substrate Fab</a></td>
</tr>
<tr>
<td class="ntdefault">
This course provides hands-on instruction in basic packaging substrate fabrication techniques, including interconnect design and testing, dielectric deposition, via formation, and metallization.  Crosslisted with CHE 4755.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     6.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4755&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4761">ECE 4761 - Industrial Ctrls &amp; Mfg</a></td>
</tr>
<tr>
<td class="ntdefault">
Students are introduced to industrial controls and the fundamentals of manufacturing with hands-on experience based on lab projects using industry software and hardware for communications and control. Crosslisted with PTFE 4761.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4781">ECE 4781 - Biomed Instrumentation</a></td>
</tr>
<tr>
<td class="ntdefault">
A study of medical instrumentation from a systems viewpoint. Pertinent physiological and electro-physiological concepts will be covered. Credit not allowed for both ECE 4781 and (CHE 4781 or CHBE 4781 or  BMED 4781 or ME 4781).
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4781&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4782">ECE 4782 - Biosystems Analysis</a></td>
</tr>
<tr>
<td class="ntdefault">
Analytical methods for modeling biological systems, including white-noise protocols for characterizing nonlinear systems. Crosslisted with BMED, CHE and ME 4782.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4783">ECE 4783 - Intro-Medical Image Proc</a></td>
</tr>
<tr>
<td class="ntdefault">
A study of mathematical methods used in medical acquisition and processing.  Concepts, algorithms, and methods associated with acquisition, processing, and display of two- and three-dimensional medical images are studied.  Crosslisted with BMED 4783.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4784">ECE 4784 - Engr Electrophysiology</a></td>
</tr>
<tr>
<td class="ntdefault">
Basic concepts of electrophysiology from an engineering perspective. Functionality of relevant organs and systems; instrumentation tools which monitor electrophysiology function. Crosslisted with BMED 4784.
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4784&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4795">ECE 4795 - GPU Prog For Video Games</a></td>
</tr>
<tr>
<td class="ntdefault">
3-D graphics pipelines. Physically-based rendering. Game engine architectures. GPU architectures. Graphics APIs. Vertex and pixel shader programming. Post-processing effects. Deferred rendering.
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>L 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4801">ECE 4801 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    1.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4802">ECE 4802 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    2.000 Credit hours
<br>
    2.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4803">ECE 4803 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4803&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4804">ECE 4804 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    4.000 Credit hours
<br>
    4.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4805">ECE 4805 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    5.000 Credit hours
<br>
    5.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4811">ECE 4811 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    1.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4812">ECE 4812 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    2.000 Credit hours
<br>
    2.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4813">ECE 4813 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4814">ECE 4814 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    4.000 Credit hours
<br>
    4.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4815">ECE 4815 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    5.000 Credit hours
<br>
    5.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4823">ECE 4823 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4833">ECE 4833 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    3.000 Credit hours
<br>
    3.000   Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4863">ECE 4863 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
Special Topics in ECE
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     2.000 Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4863&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4871">ECE 4871 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    2.000   Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4871&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4872">ECE 4872 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
Special Topics in ECE.
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     2.000 Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4873">ECE 4873 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     6.000 Lab hours
<br>
    0.000 OR     2.000 Other hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4873&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4881">ECE 4881 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4882">ECE 4882 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4883">ECE 4883 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4884">ECE 4884 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4891">ECE 4891 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 Credit hours
<br>
    3.000   Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4892">ECE 4892 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     2.000 Credit hours
<br>
    0.000 OR     1.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4893">ECE 4893 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     3.000 Credit hours
<br>
    0.000 OR     2.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4894">ECE 4894 - Special Topics</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    0.000 OR     4.000 Credit hours
<br>
    0.000 OR     3.000 Lecture hours
<br>
    0.000 OR     3.000 Lab hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4900">ECE 4900 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4901">ECE 4901 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4901&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4902">ECE 4902 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4902&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4903">ECE 4903 - Special Problems</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>ALP 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4903&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4951">ECE 4951 - Undergrad Research I</a></td>
</tr>
<tr>
<td class="ntdefault">
Participation in an individual or group research project under the direction of a faculty member.
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>P 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4951&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences, Res/CP  ≤ 30 cont hrs 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4952">ECE 4952 - Undergrad Research II</a></td>
</tr>
<tr>
<td class="ntdefault">
Participation in an individual or group research project under the direction of a faculty member.
<br>
    1.000 TO    21.000 Credit hours
<br>
    1.000 TO    21.000 Lecture hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>L 
<br>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_listcrse?term_in=202008&amp;subj_in=ECE&amp;crse_in=4952&amp;schd_in=%">All Sections for this Course</a>
<br>
<br>
Sch/Electrical &amp; Computer Engr Department
<br>
<br>
<span class="fieldlabeltext">Course Attributes: </span><br>Tech Elect CS, Engr, &amp;Sciences, Res/CP 31-50 cont hrs 
<br>
<br>
</td></tr><tr>
<td class="nttitle" scope="colgroup"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&amp;subj_code_in=ECE&amp;crse_numb_in=4XXX">ECE 4XXX - Elec/Comp Engr Elective</a></td>
</tr>
<tr>
<td class="ntdefault">
<br>
    1.000 TO    21.000 Credit hours
<br>
<br>
<span class="fieldlabeltext">Grade Basis: </span>T 
<br>
Dept/Registrar Department
<br>
<br>
</td></tr></tbody></table>
<br>
<form action="https://oscar.gatech.edu/pls/bprod/bwckctlg.xml" method="POST" name="XML">
<input type="hidden" name="term_in" value="202008">
<input type="hidden" name="subj_in" value="	ECE	">
<input type="hidden" name="title_in" value="%%">
<input type="hidden" name="divs_in" value="%">
<input type="hidden" name="dept_in" value="%">
<input type="hidden" name="coll_in" value="%">
<input type="hidden" name="schd_in" value="%">
<input type="hidden" name="levl_in" value="%">
<input type="hidden" name="attr_in" value="%">
<input type="hidden" name="crse_strt_in" value="3000">
<input type="hidden" name="crse_end_in" value="5000">
<input type="hidden" name="cred_from_in" value="">
<input type="hidden" name="cred_to_in" value="">
<input type="hidden" name="last_updated" value="">
<table class="datadisplaytable" summary="This is for formatting of the bottom links." width="50%">
<tbody><tr>
<td class="ntdefault">
<a href="javascript:history.go(-1)" onmouseover="window.status=&#39;Return to Previous&#39;;  return true" onfocus="window.status=&#39;Return to Previous&#39;;  return true" onmouseout="window.status=&#39;&#39;;  return true" onblur="window.status=&#39;&#39;;  return true">Return to Previous</a>
</td>
<td class="ntdefault"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg">New Search</a></td>
<td class="ntdefault">
</td><td class="ntdefault"><a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.xml" onclick="javascript: XML.submit();return false">XML Extract</a></td>

</tr>
</tbody></table>
</form>

<!--  ** START OF twbkwbis.P_CloseDoc **  -->
<table class="plaintable" summary="This is table displays line separator at end of the page." width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="bgtabon" width="100%" colspan="2"><img src="./Catalog Entries_files/web_transparent.gif" alt="Transparent Image" class="headerImg" title="Transparent Image" name="web_transparent" hspace="0" vspace="0" border="0" height="3" width="10"></td></tr></tbody></table>
<a href="https://oscar.gatech.edu/pls/bprod/bwckctlg.p_display_courses#top" onmouseover="window.status=&#39;Skip to top of page&#39;; return true" onmouseout="window.status=&#39;&#39;; return true" onfocus="window.status=&#39;Skip to top of page&#39;; return true" onblur="window.status=&#39;&#39;; return true" class="skiplinks">Skip to top of page</a>
</div>
<div class="footerbeforediv">

</div>
<div class="footerafterdiv">

</div>
<div class="globalafterdiv">

</div>
<div class="globalfooterdiv">

</div>
<div class="pagefooterdiv">
<span class="releasetext">Release: 8.7.2.4GT</span>
</div>
<div class="poweredbydiv">
</div>
<div class="div1"></div>
<div class="div2"></div>
<div class="div3"></div>
<div class="div4"></div>
<div class="div5"></div>
<div class="div6"></div>
<div class="banner_copyright"> <br><h5>© 2020 Ellucian Company L.P. and its affiliates.<br></h5></div>


</body></html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')

# courses = soup.find_all(class_='nttitle')

# courses = soup.find_all(class_='nttitle')

for course in soup.select('.nttitle'):
    print(course.get_text())

print(courses)