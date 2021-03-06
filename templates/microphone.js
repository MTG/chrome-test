var audio = document.querySelector('audio');

    var constraints = window.constraints = {
      audio: true,
      video: false
    };

    function handleSuccess(stream) {
      var audioTracks = stream.getAudioTracks();
      console.log('Got stream with constraints:', constraints);
      console.log('Using audio device: ' + audioTracks[0].label);
      stream.oninactive = function() {
        console.log('Stream ended');
      };
      window.stream = stream; // make variable available to browser console
      audio.srcObject = stream;
    }

    function handleError(error) {
      console.log('navigator.getUserMedia error: ', error);
      if (error.name == "NotAllowedError"){
          var message = document.getElementById("message");
          message.innerHTML = "Microphone not accessible";
      }
    }

    navigator.mediaDevices.getUserMedia(constraints).
        then(handleSuccess).catch(handleError);