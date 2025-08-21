// Client-side logic for dataset catalog and detail pages

document.addEventListener('DOMContentLoaded', () => {
  const listEl = document.getElementById('dataset-list');
  const detailEl = document.getElementById('dataset-detail');

  if (listEl) {
    fetch('/api/datasets')
      .then(r => r.json())
      .then(datasets => {
        datasets.forEach(ds => {
          const card = document.createElement('div');
          card.className = 'border rounded p-4 hover:bg-gray-50 cursor-pointer';
          card.innerHTML = `<h3 class="font-semibold">${ds.name}</h3><p>${ds.description}</p>`;
          card.addEventListener('click', () => {
            window.location.href = `/datasets/${ds.id}`;
          });
          listEl.appendChild(card);

          const wsUrl = `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws/datasets?dataset_id=${ds.id}`;
          try {
            const ws = new WebSocket(wsUrl);
            ws.addEventListener('message', e => {
              const data = JSON.parse(e.data);
              console.log('dataset update', ds.id, data);
            });
          } catch (err) {
            console.error('WebSocket error', err);
          }
        });
      })
      .catch(err => console.error('Failed to load datasets', err));
  }

  if (detailEl) {
    const datasetId = detailEl.dataset.id;
    fetch(`/api/datasets/${datasetId}`)
      .then(r => r.json())
      .then(ds => {
        detailEl.innerHTML = `<h2 class="text-xl font-bold mb-2">${ds.name}</h2><p>${ds.description}</p>`;
      });

    const wsUrl = `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws/datasets?dataset_id=${datasetId}`;
    try {
      const ws = new WebSocket(wsUrl);
      ws.addEventListener('message', e => {
        const data = JSON.parse(e.data);
        const p = document.createElement('p');
        p.className = 'text-sm text-gray-500';
        p.textContent = data.message;
        detailEl.appendChild(p);
      });
    } catch (err) {
      console.error('WebSocket error', err);
    }
  }
});
