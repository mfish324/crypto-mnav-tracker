# Progressive Web App (PWA) Setup Guide

Your crypto mNAV tracker is now a Progressive Web App! Users can install it on their phones like a native app.

## What's Been Added

✅ **PWA Manifest** - `/static/manifest.json`
✅ **Service Worker** - `/static/service-worker.js`
✅ **App Icons** - 192x192 and 512x512 PNG icons
✅ **iOS Support** - Apple-specific meta tags
✅ **Offline Support** - Basic caching for offline viewing

---

## How Users Install the App

### On Android (Chrome/Edge)

1. Visit: https://crypto-mnav-tracker.onrender.com
2. Tap the **"⋮"** menu (three dots)
3. Tap **"Install app"** or **"Add to Home screen"**
4. Confirm installation
5. App appears on home screen like a native app!

**Alternative:**
- Look for **install prompt** banner at bottom of screen
- Tap "Install" when prompted

### On iPhone/iPad (Safari)

1. Visit: https://crypto-mnav-tracker.onrender.com
2. Tap the **Share** button (box with arrow)
3. Scroll down and tap **"Add to Home Screen"**
4. Edit name if desired
5. Tap **"Add"**
6. App appears on home screen!

### On Desktop (Chrome/Edge)

1. Visit: https://crypto-mnav-tracker.onrender.com
2. Look for **install icon** in address bar (computer with arrow)
3. Click **"Install"**
4. App opens in its own window
5. Added to Start Menu/Dock!

---

## PWA Features

### Standalone Mode
- Runs in full-screen without browser UI
- Looks like a native app
- Custom app icon
- Separate window from browser

### Offline Support
- Basic caching of app shell
- Can view last loaded data offline
- Automatic updates when online

### Fast Loading
- Service worker caches resources
- Near-instant load on repeat visits
- Reduced data usage

### Native-Like Experience
- Add to home screen
- Custom splash screen
- Status bar theming (cyan!)
- Portrait orientation lock

---

## Testing the PWA

### Check PWA Readiness

**Chrome DevTools:**
1. Open https://crypto-mnav-tracker.onrender.com
2. F12 to open DevTools
3. Go to **"Application"** tab
4. Check **"Manifest"** section:
   - ✅ Name: "Crypto Treasury mNAV Tracker"
   - ✅ Icons: 192px and 512px
   - ✅ Start URL: "/"
   - ✅ Theme color: #00ffff

5. Check **"Service Workers"** section:
   - ✅ Status: Activated
   - ✅ Source: /static/service-worker.js

**Lighthouse Audit:**
1. DevTools → **"Lighthouse"** tab
2. Select **"Progressive Web App"**
3. Click **"Analyze page load"**
4. Should score 90+ out of 100!

---

## What Makes It Work

### 1. Manifest File (`/static/manifest.json`)
Defines app properties:
- Name and short name
- Icons for different sizes
- Background/theme colors
- Display mode (standalone)
- Orientation preference

### 2. Service Worker (`/static/service-worker.js`)
Enables:
- Offline functionality
- Background sync
- Push notifications (future)
- Resource caching

### 3. Meta Tags (in `index.html`)
Provides:
- iOS compatibility
- Theme colors
- App capabilities
- Description for app stores

---

## Customization Options

### Change App Colors

Edit `manifest.json`:
```json
{
  "theme_color": "#00ffff",  // Address bar color
  "background_color": "#0a0a0a"  // Splash screen
}
```

### Update App Name

Edit `manifest.json`:
```json
{
  "name": "Your Full App Name",
  "short_name": "Short Name"  // Used on home screen
}
```

### Custom Icons

Replace `/static/icon-192.png` and `/static/icon-512.png` with your own:
- Must be PNG format
- Sizes: 192x192 and 512x512 pixels
- Square dimensions
- Clear, simple design works best

Re-generate with custom design:
```bash
python generate_icons.py
```

---

## Share with Beta Testers

### Quick Share Message:

**Text/Email:**
```
Try the Crypto Treasury mNAV Tracker app!

📱 Install on your phone:
1. Visit: https://crypto-mnav-tracker.onrender.com
2. Android: Tap menu → "Install app"
3. iPhone: Tap share → "Add to Home Screen"

Tracks mNAV for BTC, ETH, SOL treasury companies in real-time!
```

**QR Code:**
Generate at: https://qr-code-generator.com
- URL: https://crypto-mnav-tracker.onrender.com
- Users scan to install instantly

---

## Troubleshooting

### "Install" option not showing

**Reasons:**
- Must use HTTPS (Render provides this ✅)
- Service worker must register successfully
- Manifest must be valid
- Not already installed

**Check:**
1. Open browser console (F12)
2. Look for service worker registration message
3. Check for errors in manifest

### App not updating

**Solution:**
1. Uninstall the app
2. Clear browser cache
3. Reinstall from website

Or update service worker cache name in `service-worker.js`:
```javascript
const CACHE_NAME = 'crypto-mnav-v2';  // Increment version
```

### Icons not showing

**Check:**
1. Files exist: `/static/icon-192.png` and `/static/icon-512.png`
2. Correct paths in `manifest.json`
3. Re-deploy to Render

Regenerate icons:
```bash
python generate_icons.py
```

---

## Next Steps

### After Beta Testing

Based on user feedback, you might want to:

1. **Add Push Notifications**
   - Alert users when mNAV changes significantly
   - Requires service worker enhancement

2. **Offline Data Storage**
   - Cache last fetched data in IndexedDB
   - View even when offline

3. **Native Apps (If Needed)**
   - Build React Native version
   - Access to more device features
   - Better performance

### Upgrade to React Native (Later)

If you need:
- Camera access
- Better performance
- Native UI components
- App store presence

We can create a separate React Native project that:
- Uses your existing API
- Shares the same backend
- Provides native mobile experience

---

## Deployment Checklist

Before sharing with beta users:

- [x] PWA files created
- [x] Icons generated
- [x] Service worker registered
- [ ] Deploy to Render
- [ ] Test installation on Android
- [ ] Test installation on iPhone
- [ ] Test offline functionality
- [ ] Share with beta testers!

---

## Files Added

```
crypto_mnav_tracker/
├── static/
│   ├── manifest.json           # PWA configuration
│   ├── service-worker.js       # Offline support
│   ├── icon-192.png           # App icon (small)
│   └── icon-512.png           # App icon (large)
├── templates/
│   └── index.html             # Updated with PWA meta tags
└── generate_icons.py          # Icon generator script
```

---

**Your app is now installable on iOS and Android! 🎉**

Deploy to Render and share the link with your beta testers!

*Last updated: November 8, 2025*
