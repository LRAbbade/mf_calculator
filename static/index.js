function mf(a1, a2, a3, a4, a5) {
    // console.log(JSON.stringify({a1, a2, a3, a4, a5}));
    const n1 = (a1 + a2 + a3) / 3;
    const n2 = 0.1 * a4 + 0.9 * a5;
    return {
        n1,
        n2,
        mf: 0.4 * n1 + 0.6 * n2
    };
}

function process() {
    const res = mf(
        Number($("#a1").val()),
        Number($("#a2").val()),
        Number($("#a3").val()),
        Number($("#a4").val()),
        Number($("#a5").val())
    );
    // console.log(JSON.stringify(res));
    $("#n1").text(res.n1);
    $("#n2").text(res.n2);
    $("#mf").text(res.mf);
}

$(document).on('keypress', (e) => {
    if(e.which == 13) {
        process();
    }
});

$(document).ready(() => {
    $("#calc").click(process);
});
