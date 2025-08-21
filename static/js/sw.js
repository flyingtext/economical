self.addEventListener('push', event => {
  const data = event.data?.json() || {};
  event.waitUntil(
    self.registration.showNotification(data.title || 'Economical', {
      body: data.message || '',
    })
  );
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
});
