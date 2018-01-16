// global session
var session = new QiSession(function(session) {
                // document.getElementById('typed').innerHTML = "Connection esterblished!";
              }, function() {
                // document.getElementById('typed').innerHTML = "Could not connect to the robot";
              });


// Subscribe to ALMemory Service   
session.service("ALMemory").then(function(ALMemory) {
  // document.getElementById('typed').innerHTML = "ALMemory proxy subscription successful!";  
  ALMemory.getData('keyword_typed').then(function(keyword){
        
        new Typed('#typed', {
          strings: [keyword],
          typeSpeed: 1,
          fadeOut: true,
        });

  });
   ALMemory.getData('keyword_CH').then(function(keyword){
        document.getElementById('Conversation_history').innerHTML = [keyword];


  });
});



