function Login()
{
	email=document.getElementById('inputemail').value;
	password=document.getElementById('inputpassword').value;
	console.log(email,password);
	$.ajax({
		type: "GET",
		url: '/get_data/',
		data:{'inputemail':email,'inputpassword':password},
		dataType:"json",
		success:function(outputdata)
		{
			console.log(">>",outputdata);
			if (outputdata['result']=='True')
				{
				console.log("hello world");
				window.location.href="http://127.0.0.1:5000/profile"
				}
			else{
				//console.log("part",outputdata);
				window.location.href="http://127.0.0.1:5000/loginpage;"
			}
		},
	    error:function(error) {
	    	console.log(error);
	    }
	   
	    });
	    console.log('exit');
	    }
			