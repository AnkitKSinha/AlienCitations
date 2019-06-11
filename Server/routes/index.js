module.exports = function(io) {
	var express = require('express');
	var router = express.Router();
	var cp = require("child_process");
	var fs = require("fs");
	// const completeData = require("../visual_data_2.json");
	let hbs = require("hbs");
	let multer = require("multer");


	let storage = multer.diskStorage({
		destination: (req, file, cb) => {
			cb(null, 'public/datasets/')
		},
		filename: (req, file, cb) => {
			cb(null, file.fieldname)
		}
	});
	let upload = multer({storage: storage});


	hbs.registerHelper('parseJson', function(context) {
		if(!context) {
			return JSON.stringify({});
		}
		return JSON.stringify(context);
	});

	/* GET home page. */
	router.get('/', function(req, res, next) {
	  res.render('index', { title: 'Express', graph : {}, histogram : {}, score : 0, aci : 0 });
	});

	router.post('/', upload.fields([{
		name : 'dataset',
		maxCount : 1
	}, {
		name : 'list',
		maxCount : 1
	}]), (req, res, next) => {
		// console.log("Files : " + JSON.stringify(req.files))
		// res.render('index', {title : "Express"});
		var q = 'python3 scripts/main.py';
		// console.log(q);
		cp.exec(q, function(err, stdout, stderr){
			if(err) {
				stdout = "Error : " + err;
				console.log(err);
			}
			if(stderr) {
				console.log("StdErr : " + stderr);
			}
			let score = 0;
			let aci = 0;
			if(stdout) {
				let lines = stdout.split("\n");
				// let histogramData = lines[0];
				score = Number(lines[0]).toFixed(3);
				aci = Number(lines[1]).toFixed(3);
				// console.log("HISTOGRAM DATA : " + JSON.parse(histogramData));
				console.log("SCORE : " + score);
				console.log("ACI : " + aci);

			}
			fs.readFile("public/results/visual_data.json",(err, data) => {
				if(err) {
					console.log(err);
				} else {
					data = JSON.parse(data);
					var nodes = [];
					var edgePairs = [];
					nodes = data.nodes;
					edgePairs = data.edges;
					var graph = {};
					graph.nodes = nodes;
					graph.edges = edgePairs;
					// res.render('index', {graph : graph});

					fs.readFile("public/results/histogram_data.json", (err, hist) => {
						if(err) {
							console.log(err);
						} else {
							hist = JSON.parse(hist);
							console.log("Hist : " + hist);
							res.render('index', {graph : graph, histogram : hist, score : score, aci : aci});
						}
					});
				}
			});
		});
	});



	// io.on("connection", function(socket){
	// 	console.log("connected");
	// 	socket.on("correct_request", function(data){
	// 		console.log(data);
	// 		// var q = 'python3 second.py "'+data+'"';
	// 		var q = 'python3 --version';
	// 		console.log(q);
	// 		cp.exec(q, function(err, stdout, stderr){
	// 			// console.log(stdout);
	// 			// if(!stdout){
	// 			// 	stdout = "I'm still in Beta, calm down!";
	// 			// }
	// 			if(err) {
	// 				stdout = "Error : " + err;
	// 				console.log(err);
	// 			}
	// 			if(stderr) {
	// 				console.log("StdErr : " + stderr);
	// 			}
	// 			var nodes = [];
	// 			var edgePairs = [];
	// 			nodes = completeData.nodes;
	// 			edgePairs = completeData.edges;
	// 			var graph = {};
	// 			graph.nodes = nodes;
	// 			graph.edges = edgePairs;

	// 			socket.emit("correct_response", graph);
	// 			console.log("socket emitted");
	// 		});
	// 	});
	// });

	return router;
};

