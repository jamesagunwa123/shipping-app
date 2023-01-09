function check(element) { 
    if (element.value==""){ 
        element.className='error'; 
    } else { element.className 
        ='form-input'; 
    } 
} 

function checkemail(element) { 
    if (element.value!=""){ 
        var data = element.value; 
        var expression = /^([a-zA-Z0-9_.-])+@(([a-zA-z0-9-])+.)+([a-zA-Z0-9-]{2 ,4})+$/; 
        if (!expression.test(data)) { 
            element.className='error'; 
        } else { element.className 
        ='form-input'; 
        } 
	} 
} 


function validate(form) { 
  if(form.name.value==""
    alert('You haven't typed your name'); // Message to display 
    return false; //we return a negative value 
  } 
  
  if(form.email.value=="") { //If this field is empty 
    alert ('You have not written your e-Mail'); // Message to display 
    return false; //we return a negative value 
  } 
  
  if(form.subject.value=="") { //If this field is empty 
    alert ('You have not written the Subject'); // Message to display 
    return false; //we return a negative value 
  } 
 
  return true; // If all is well, we return Ok, positive 
}