document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search');
  const checkboxes = document.querySelectorAll('.filter-checkbox');
  const cards = document.querySelectorAll('.category-card');

  function applyFilters() {
    const query = searchInput.value.toLowerCase();
    const active = Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    cards.forEach(card => {
      const text = card.innerText.toLowerCase();
      const adaptability = card.dataset.adaptability;
      const matchesQuery = text.includes(query);
      const matchesAdaptability = active.length === 0 || active.includes(adaptability);
      card.style.display = matchesQuery && matchesAdaptability ? '' : 'none';
    });
  }

  searchInput.addEventListener('input', applyFilters);
  checkboxes.forEach(cb => cb.addEventListener('change', applyFilters));
});
