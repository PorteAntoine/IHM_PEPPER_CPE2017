// global session
var session = new QiSession(function(session) {
                // document.getElementById('typed').innerHTML = "Connection esterblished!";
              }, function() {
                // document.getElementById('typed').innerHTML = "Could not connect to the robot";
              });


// Subscribe to ALMemory Service   
session.service("ALMemory").then(function(ALMemory) {
  // document.getElementById('typed').innerHTML = "ALMemory proxy subscription successful!";  
   ALMemory.getData('titre').then(function(keyword){
        document.getElementById('titre').innerHTML = [keyword];
  });
   ALMemory.getData('txt1').then(function(keyword){
        document.getElementById('txt1').innerHTML = [keyword];
  });
   ALMemory.getData('txt2').then(function(keyword){
        document.getElementById('txt2').innerHTML = [keyword];
  });
   ALMemory.getData('txt3').then(function(keyword){
        document.getElementById('txt3').innerHTML = [keyword];
  });
  ALMemory.getData('pourcentage').then(function(keyword){
        document.getElementById('meter').value = [keyword];
  });
});



