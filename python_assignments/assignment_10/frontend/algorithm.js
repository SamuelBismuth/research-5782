function createMatrix() {
    let n = document.getElementById('number_n').value
    let m = document.getElementById('number_m').value
    createTable(m, n, 'A')
    createTable(m, 1, 'b')
    createTable(1, n, 'c')
}

function createTable(num_rows, num_cols, id) {
    var theader = '<table border="1">\n';
    var tbody = '';

    for (var i = 0; i < num_rows; i++) {
        tbody += '<tr>';
        for (var j = 0; j < num_cols; j++) {
            tbody += '<td class="matrix' + id + '">';
            tbody += '<input type="number" name="number" value="" />';
            tbody += '</td>'
        }
        tbody += '</tr>\n';
    }
    var tfooter = '</table>';
    document.getElementById(id).innerHTML = theader + tbody + tfooter;
}

function retrieveInputMatrix(num_rows, num_cols, id) {
    var matrix = [];
    var arr = document.getElementsByClassName(id);

    if (arr.length == 0) {
        alert('Please, first, fill the matrixes.')
        throw new Error('Please, first, fill the matrixes.');
    }

    let count = 0
    for (var i = 0; i < num_rows; i++) {
        line = [];
        for (var j = 0; j < num_cols; j++) {
            entry = parseInt(arr[count].firstChild.value)
            if (entry != 0 && entry == '' || isNaN(entry)) {
                alert('At least one entry is not valid.')
                throw new Error('At least one entry is not valid.');
            } else {
                count++
                line.push(entry)
            }
        }
        matrix.push(line);
    }
    return matrix
}

function retrieveInputMatrixes() {
    let n = document.getElementById('number_n').value
    let m = document.getElementById('number_m').value

    var A = retrieveInputMatrix(m, n, 'matrixA');
    var b = retrieveInputMatrix(1, m, 'matrixb');
    var c = retrieveInputMatrix(1, n, 'matrixc');

    return JSON.stringify({
        'A': A,
        'b': b,
        'c': c
    })
}


function runAlgorithm() {
    let data = retrieveInputMatrixes()

    var wait = document.getElementById("wait");
    wait.style.display = "block";

    let BACKEND_PORT = 8080;

    let httpurl = "http://" + location.hostname + ":" + BACKEND_PORT + "/"

    $.ajax({
        url: httpurl + "run_algorithm/",
        type: "POST",
        contentType: 'application/json',
        data: data,
        dataType: 'json',
        complete: function (xmlHttp) {
            window.location = 'output.html?output='+xmlHttp.responseText;
        }
    }).done(function (data) {
    });
}