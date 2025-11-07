const apiUrl = "http://127.0.0.1:8000/analyze";

document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const text = document.getElementById("inputText").value;
  if (!text.trim()) {
    alert("Please enter some text!");
    return;
  }

  const res = await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  const data = await res.json();
  document.getElementById("result").classList.remove("hidden");

  // Style
  document.getElementById("style").textContent = data.style;

  // Readability
  const r = data.readability;
  document.getElementById("readability").innerHTML = `
    <li>Flesch Reading Ease: <b>${r.flesch_reading_ease}</b></li>
    <li>Flesch–Kincaid Grade: <b>${r.flesch_kincaid_grade}</b></li>
    <li>Avg Sentence Length: <b>${r.avg_sentence_length}</b></li>
    <li>Lexical Diversity: <b>${r.lexical_diversity}</b></li>
  `;

  // Tone
  const t = data.tone;
  const polarityLabel = t.polarity > 0 ? "Positive" : (t.polarity < 0 ? "Negative" : "Neutral");
  const subjLabel = t.subjectivity > 0.5 ? "Personal" : "Objective";

  document.getElementById("tone").innerHTML = `
    <li>Polarity: <b>${t.polarity}</b> (${polarityLabel})</li>
    <li>Subjectivity: <b>${t.subjectivity}</b> (${subjLabel})</li>
  `;
});