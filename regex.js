var classDict = {"ece 2020": "false", "ece 2030": "false", "ece 2035": "true",
"ece 2036": "false", "cs 1372": "false", "cs 2110": "false"}; //should be replaced with the info from DegreeWorks
var txt = "(ece 2020 || ece 2030) && (ece 2035 || ece 2036 || cs 1372) || cs 2110"; //the prerequisite text from Buzzport
var pattern = new RegExp("\\w{2,4}[\\s]\\w{4,4}", "g") //the regular expression that finds class names within text
var matches = txt.match(pattern); // returns an array with all class prerequisites
var needToTake = []
matches.forEach(replacement); //for each class prerequisite in the array, replace it in the string with
                              // true if taken, false if not (based on dictionary from DegreeWorks)
var reqsSatisfied = eval(txt); //evaluates whether the prereqs have been satisfied
if (!reqsSatisfied) { //if they haven't returns a list of the prerequisites that have not been satisfied
  matches.forEach(unsatisfied)
}
console.log("You have prerequisites that are currently unsatisfied: " + needToTake);


function replacement(item) {
  txt = txt.replace(item, classDict[item]);
}

function unsatisfied(item) {
  if (!eval(classDict[item])) {
    needToTake.push(item);
  }
}
