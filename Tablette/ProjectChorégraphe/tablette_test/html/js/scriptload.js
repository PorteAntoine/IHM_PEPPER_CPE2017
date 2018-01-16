window.onload = function (){
    // global session
    var session = new QiSession(function(session) {
                    // document.getElementById('typed').innerHTML = "Connection esterblished!";
                  }, function() {
                    // document.getElementById('typed').innerHTML = "Could not connect to the robot";
                  });


    // Subscribe to ALMemory Service
    session.service("ALMemory").then(function(ALMemory) {
      // document.getElementById('typed').innerHTML = "ALMemory proxy subscription successful!";
      var txt =  ALMemory.getData('keyword')
      document.getElementById('descriptif_produit').innerHTML = txt;

    });
}




