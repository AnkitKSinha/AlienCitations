$(document).ready(function(){
	$("#dataset-button").click((e) => {
		$("#dataset-upload").trigger("click");
	});
	$("#list-button").click((e) => {
		$("#list-upload").trigger("click");
	});


	$("#dataset-upload").on("change", (e)=> {
		let selectedFile = $("#dataset-upload").val();
		if(selectedFile) {
			$(".file-selected-text").text(selectedFile);
		}
	});

	$("#list-upload").on("change", (e)=> {
		let selectedFile = $("#list-upload").val();
		if(selectedFile) {
			$(".list-selected-text").text(selectedFile);
		}
	});

	$("#dataset-upload").on("change", (e)=> {
		let selectedFile = $("#dataset-upload").val();
		if(selectedFile) {
			$(".file-selected-text").text(selectedFile);
		}

	});
	
	// console.log("dataset : " + $("#dataset-upload").val());
	var socket = io();
	$("#sentence").focus();
	
	$("#sentence").keypress(function(e){
		if(e.which == 13){
			// alert("here");
			$("#enter").click();
		}
	});
	
	$("#start-button").click(function(){
		// alert("button pressed");
		var t = $("#sentence").val();
		socket.emit("correct_request", t);
	});

	
	// socket.on("correct_response", function(graph){
	// 	var nodes = new vis.DataSet();
	// 	console.log("Graph : " + JSON.stringify(graph));
	// 	var graphInitNodes = graph.nodes;
	// 	nodes.add(graphInitNodes);
	// 	// create an array with edges
	// 	var edges = graph.edges;
	// 	// create a network
	// 	var container = document.getElementById('mynetwork');
	// 	// provide the data in the vis format
	// 	var data = {
	// 		nodes: nodes,
	// 		edges: edges
	// 	};
	// 	var options = {
	// 		nodes:{
	// 			shape : "circle",
	// 			borderWidth: 1,
	// 			borderWidthSelected: 2,
	// 			brokenImage:undefined,
	// 			chosen: true,
	// 			font: {
	// 				color: '#000',
	// 			}
	// 		}
	// 	};
	// 	// initialize your network!
	// 	var network = new vis.Network(container, data, options);
		
	// });
});