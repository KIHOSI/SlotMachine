var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var exec = require('child_process').exec;
app.use(bodyParser.urlencoded());

app.get('/', function (req, res) { //一開始，就回傳index.html
   res.sendFile('/home/pi/SlotMachineFile/index.html'); //absolute path
   exec('python SlotMachine.py ',function(err,stdout,stderr){ //initailize SlotMachine.py
		if(err){
			console.log('stderr',err);
		}
		if(stdout){
			console.log('stdout',stdout);
		}
	}); 
})

app.post('/slotmachine',function(req,res){ //執行SlotMachine.py
	console.log("callSlotMachine");
	exec("python -c 'import SlotMachine; SlotMachine.gameStart()'",function(err,stdout,stderr){
		if(err){
			console.log('stderr',err);
		}
		if(stdout){
			console.log('stdout',stdout);
		}
	}); 
});

app.post('/gameover',function(req,res){ //遊戲結束，關閉7節管
	console.log('works');
	exec("python -c 'import SlotMachine; SlotMachine.closeSegement()'",function(err,stdout,stderr){
		if(err){
			console.log('stderr',err);
		}
		if(stdout){
			console.log('stdout',stdout);
		}
	}); 
});

app.listen(8080);
