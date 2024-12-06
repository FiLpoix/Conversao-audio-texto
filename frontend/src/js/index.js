const transcreverAudio = document.querySelector('.transcrever-audioBtn');
const transcreverAudioSection = document.querySelector('#transcrever-audio')
const converterAudio = document.querySelector('.converter-audioBtn');
const converterAudioSection = document.querySelector('#converter-audio');

transcreverAudio.addEventListener('click', function(){
    if (transcreverAudioSection.style.display === 'none') {
        transcreverAudioSection.style.display = 'block';
        converterAudioSection.style.display = 'none'
    } else {
        transcreverAudioSection.style.display = 'none';
        converterAudioSection.style.display = 'block';
    }
})