<?php 

if($_GET['get_status'] == 'clicked'){
    $value = array("message"=>"user clicks");
}
else{
    $value = array("message"=>"Nothing happens");
}

echo json_encode($value);
?>