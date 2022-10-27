// リアルタイムに取得
let hue_min_range = document.querySelector(`input[type='range'][name='hue_min_range']`);
let hue_max_range = document.querySelector(`input[type='range'][name='hue_max_range']`);
let sat_min_range = document.querySelector(`input[type='range'][name='sat_min_range']`);
let sat_max_range = document.querySelector(`input[type='range'][name='sat_max_range']`);
hue_min_range.addEventListener(`input`, () => {
	document.querySelector(`#hue_min_output`).innerHTML = `HUE_MIN:${hue_min_range.value}`;
});

hue_max_range.addEventListener(`input`, () => {
	document.querySelector(`#hue_max_output`).innerHTML = `HUE_MAX:${hue_max_range.value}`;
});
// リアルタイムに取得

sat_min_range.addEventListener(`input`, () => {
	document.querySelector(`#sat_min_output`).innerHTML = `SAT_MIN:${sat_min_range.value}`;
});

sat_max_range.addEventListener(`input`, () => {
	document.querySelector(`#sat_max_output`).innerHTML = `SAT_MAX:${sat_max_range.value}`;
});