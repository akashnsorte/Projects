document.addEventListener('DOMContentLoaded', function () {
    // Check the user's preference for dark mode
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    // Set the initial mode based on user preference
    document.body.classList.toggle('dark-mode', prefersDarkMode);

    // Update mode when the toggle is clicked
    document.getElementById('darkModeToggle').addEventListener('change', function () {
        document.body.classList.toggle('dark-mode');
    });
});
