document.querySelectorAll(".copy-btn").forEach(button => {
    button.addEventListener('click', () => {
        const code = button.closest('.code-header').nextElementSibling.querySelector('code').textContent.trim();
        const textToCopy = code.replace(/^\$\s*/, '')
        navigator.clipboard.writeText(textToCopy).then(() => {
            button.textContent = 'Copied!';
            setTimeout(() => {
                button.textContent = 'Copy';
            }, 2000)
        })
    })
})