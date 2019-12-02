$(document).ready(function() {
    $('form').submit(function(event) {
        const grade = parseFloat($("input[name=성적정보]").val());
        const credit = parseFloat($("input[name=이수학점]").val());

        if(isNaN(grade)) {
            alert("성적 정보에 숫자를 입력해주세요");
            event.preventDefault();
            return;
        }

        if(grade > 4.5 || grade < 0) {
            alert("0에서 4.5 사이의 값을 입력해주세요");
            event.preventDefault();
            return;
        }

        if(isNaN(credit)) {
            alert("이수 학점에 숫자를 입력해주세요");
            event.preventDefault();
            return;
        }
    });
});
