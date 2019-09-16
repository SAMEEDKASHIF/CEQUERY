<!DOCTYPE html>
<html lang="en-US">
<head>
<title>download file</title>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/0.9.0rc1/jspdf.min.js"></script>
</head>
<body>
<!-- Content Area -->
<div id="print">
     <h3>CEQUERY</h3>
     
</div>
<div id="print-btn"></div>
<button id="submit">Download PDF File</button>
<!-- Script -->
 

var doc = new jsPDF();
var specialElementHandlers = {
    '#print-btn': function (element, renderer) {
        return true;
    }
};

$('#submit').click(function () {
    doc.fromHTML($('#print').html(), 15, 15, {
        'width': 170,
            'elementHandlers': specialElementHandlers
    });
    doc.save('pdf-version.pdf');
});
 

</body>
</html>