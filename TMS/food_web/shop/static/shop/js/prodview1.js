
	var durationnn;
	var qunatityyy;
	var m=1;
	document.getElementById('lunch').addEventListener('click',function(){
	    document.getElementById('lunch1').value= 'lunch';
		document.getElementById('calc').style.display = "block";
		document.getElementById('time').innerHTML = "Details For Lunch<hr>";
		console.log('clicked');
	});
	document.getElementById('dinner').addEventListener('click',function(){
	    document.getElementById('lunch1').value= 'dinner';
		document.getElementById('calc').style.display = "block";
		document.getElementById('time').innerHTML = "Details For dinner<hr>";
	})
	document.getElementById('both').addEventListener('click',function(){
	    document.getElementById('lunch1').value= 'both';
		document.getElementById('calc').style.display = "block";
		document.getElementById('time').innerHTML = "Details For lunch <br><hr> Details For dinner<hr>";
	})
	document.querySelector('week').addEventListener('click',function(){
		document.getElementById('duration').innerHTML = "Duration                     One week";
		m=1;
	});
	document.querySelector('onem').addEventListener('click',function(){
		document.getElementById('duration').innerHTML = "Duration                     One mounth";
		m=4;
	});
	document.querySelector('twom').addEventListener('click',function(){
		document.getElementById('duration').innerHTML = "Duration                     Two mounth";
		m=8;
	});
	document.querySelector('sixweek').addEventListener('click',function(){
		document.getElementById('days').innerHTML = "Week Type                  Six Days";
		durationnn=6;
	})
	document.querySelector('sevenweek').addEventListener('click',function(){
		document.getElementById('days').innerHTML = "Week Type                  Seven Days";
		durationnn=7;
	})
	document.querySelector('quaone').addEventListener('click',function(){
		document.getElementById('quan').innerHTML = "Quantity                     One";
		qunatityyy=1;
		var price=95*durationnn*qunatityyy*m;
		var tax=Math.floor(price/6);
		var del=30*durationnn;
		var total=price+tax+del
		document.getElementById('price').innerHTML = `Price                          ${price}`;
		document.getElementById('tax').innerHTML = `Tax                            ${tax}`;
		document.getElementById('del').innerHTML = `Delivery Charge          ${del}<hr>`;
		document.getElementById('total').innerHTML = `Grand Total                ${total}`;
	})
	document.querySelector('quatwo').addEventListener('click',function(){
		document.getElementById('quan').innerHTML = "Quantity                     Two";
		qunatityyy=2;
		var price=95*durationnn*qunatityyy*m;
		var tax=Math.floor(price/6);
		var del=30*durationnn;
		var total=price+tax+del
		document.getElementById('price').innerHTML = `Price                          ${price}`;
		document.getElementById('tax').innerHTML = `Tax                            ${tax}`;
		document.getElementById('del').innerHTML = `Delivery Charge          ${del}<hr>`;
		document.getElementById('total').innerHTML = `Grand Total                ${total}`;

	})
	document.querySelector('quathree').addEventListener('click',function(){
		document.getElementById('quan').innerHTML = "Quantity                     Three";
		qunatityyy=3;
		var price=95*durationnn*qunatityyy*m;
		var tax=Math.floor(price/6);
		var del=30*durationnn;
		var total=price+tax+del
		document.getElementById('price').innerHTML = `Price                          ${price}`;
		document.getElementById('tax').innerHTML = `Tax                            ${tax}`;
		document.getElementById('del').innerHTML = `Delivery Charge          ${del}<hr>`;
		document.getElementById('total').innerHTML = `Grand Total                ${total}`;
	})



