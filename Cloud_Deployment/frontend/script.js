document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('processForm');
    const urlInput = document.getElementById('urlInput');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.querySelector('.btn-text');
    const btnLoader = document.querySelector('.btn-loader');

    const resultsSection = document.getElementById('resultsSection');
    const errorBanner = document.getElementById('errorBanner');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const url = urlInput.value.trim();
        if (!url) return;

        // Reset state
        errorBanner.classList.add('hidden');
        resultsSection.classList.add('hidden');

        // Setup Loading State
        btnText.style.display = 'none';
        btnLoader.style.display = 'block';
        submitBtn.disabled = true;

        try {
            const response = await fetch('https://dcc-lca-02.vercel.app/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: url })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();

            // Populate results
            document.getElementById('resultTitle').textContent = data.title || 'Untitled Page';
            document.getElementById('resultSummary').textContent = data.summary || 'No summary could be generated.';

            // Show results
            resultsSection.classList.remove('hidden');

        } catch (error) {
            console.error('Processing error:', error);
            document.getElementById('errorMessage').textContent = `Failed to process the URL. Ensure the backend is running. ${error.message}`;
            errorBanner.classList.remove('hidden');
        } finally {
            // Revert Loading State
            btnText.style.display = 'block';
            btnLoader.style.display = 'none';
            submitBtn.disabled = false;
        }
    });
});
