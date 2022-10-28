var video= document.getElementById('video');
var media = navigator.mediaDevices.getUserMedia({video:true});

media.then((stream)=>{
    video.srcObject = stream;
});

var canvas = document.getElementById('canvas');
canvas.setAttribute('width', video.width);
canvas.setAttribute('height', video.height);


video.addEventListener(
    'timeupdate',
    function () {
        var context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, video.width, video.height);
    },
    true
);

document.addEventListener('keydown', (event) => {
    var keyName = event.key;
    if (keyName === ' ') {
        console.log(`keydown: SpaceKey`);
        context = canvas.getContext('2d');
        // 取得したbase64データのヘッドを取り除く
        var img_base64 = canvas.toDataURL().replace(/^.*,/, '')
        captureImg(img_base64);
    }
});

var xhr = new XMLHttpRequest();
var image_to_embed = "";

// キャプチャ画像データ(base64)をPOST
function captureImg(img_base64) {
    const body = new FormData();
    body.append('img', img_base64);
    body.append('min_hue',hue_min_range.value);
    body.append('max_hue',hue_max_range.value);
    body.append('min_sat',sat_min_range.value);
    body.append('max_sat',sat_max_range.value);
    body.append('judge_mani_black',judge_mani_black.value);
    body.append('detect_min_bright',detect_bright.value);
    xhr.open('POST', 'http://localhost:8000/transparent/', true);
    xhr.onload = () => {
        image_to_embed = "data:image/png;base64," + xhr.responseText.slice(1,-1);
        //ダブルクォーテーションが邪魔なので前後削除
        $('.image').children('img').attr('src',image_to_embed);
    };
    xhr.send(body);
}

function DownloadImage(){
    var nowtime = new Date();
    downloadbutton = document.getElementById('downloadbutton');
    downloadbutton.href = image_to_embed;
    downloadbutton.download = nowtime.getHours()+"_"+nowtime.getMinutes()+"_"+nowtime.getSeconds();

}

let hue_min_range = document.querySelector(`input[type='range'][name='hue_min_range']`);
let hue_max_range = document.querySelector(`input[type='range'][name='hue_max_range']`);
let sat_min_range = document.querySelector(`input[type='range'][name='sat_min_range']`);
let sat_max_range = document.querySelector(`input[type='range'][name='sat_max_range']`);
let detect_bright = document.querySelector(`input[type='range'][name='bright']`);
let judge_mani_black = document.querySelector(`input[type='checkbox'][name='judge_manipulation_black']`);
hue_min_range.addEventListener(`input`, () => {
	document.querySelector(`#hue_min_output`).innerHTML = `HUE_MIN:${hue_min_range.value}`;
});

hue_max_range.addEventListener(`input`, () => {
	document.querySelector(`#hue_max_output`).innerHTML = `HUE_MAX:${hue_max_range.value}`;
});

sat_min_range.addEventListener(`input`, () => {
	document.querySelector(`#sat_min_output`).innerHTML = `SAT_MIN:${sat_min_range.value}`;
});

sat_max_range.addEventListener(`input`, () => {
	document.querySelector(`#sat_max_output`).innerHTML = `SAT_MAX:${sat_max_range.value}`;
});

detect_bright.addEventListener(`input`,()=>{
    document.querySelector(`#bright_output`).innerHTML = `MIN_BRGT:${detect_bright.value}`;
})
