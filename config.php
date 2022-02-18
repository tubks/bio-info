<?php
$con = oci_connect("jradola_a", 'jradola_a', 'dbinfo');
if (!con) {
    echo "Connection failed" . oci_error();
}
?> 