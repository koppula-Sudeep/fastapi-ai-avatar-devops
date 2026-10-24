
const button = document.getElementById("speakButton");
const message = document.getElementById("message");
const audio = document.getElementById("audio");
const status = document.getElementById("status");

button.addEventListener("click", async () => {
    button.disabled = true;
    status.textContent = "Preparing my introduction...";

    try {
        const response = await fetch("/api/introduction");

        if (!response.ok) {
            throw new Error("Could not load the introduction");
        }

        const data = await response.json();

        message.textContent = data.message;
        audio.src = data.audio_url;

        await audio.play();
        status.textContent = "Speaking...";

    } catch (error) {
        console.error(error);
        status.textContent =
            "Unable to play audio. Check your internet connection and try again.";
    } finally {
        button.disabled = false;
    }
});

audio.addEventListener("ended", () => {
    status.textContent = "Introduction complete. Nice to meet you!";
});

audio.addEventListener("error", () => {
    status.textContent = "Audio playback failed. Please try again.";
});
