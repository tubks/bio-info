<?php
include("config.php");
echo "działa " . $_POST["search"];
if($isset($_POST['search']))    {
    $acc_to_search = $_POST['search'];
    $stid = oci_parse($con, "SELECT P.seq, P.seqLength, P.seqMass, E.specie FROM ENTRIES E, PROTEINS P WHERE P.accession LIKE'$acc_to_search'");
    
    oci_define_by_name($stid, 'P.seq', $seq);
    oci_define_by_name($stid, 'P.seqLength', $seqLength);
    oci_define_by_name($stid, 'P.seqMass', $seqMass);
    oci_define_by_name($stid, 'E.specie', $specie);

    oci_execute($stid);

    oci_fetch($stid);
    echo "seq: $seq length: $seqLength mass: $seqMass<br>\n";
    echo "<a href='https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=$specie'>https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=$specie</a>";
oci_free_statement($stid);
oci_close($conn);
    }
?>