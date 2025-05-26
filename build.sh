#!/bin/bash

# Snake Game Build Script
echo "🐍 Building Snake Game with Pygbag..."

# Check if pygbag is installed
if ! command -v pygbag &> /dev/null; then
    echo "❌ Pygbag not found. Installing..."
    pip install pygbag
fi

# Clean previous build
if [ -d "dist" ]; then
    echo "🧹 Cleaning previous build..."
    rm -rf dist/
fi

# Build the game
echo "🔨 Building game..."
python -m pygbag --archive --cdn https://cdn.jsdelivr.net/pyodide/ main.py

# Check if build was successful
if [ -d "dist" ]; then
    echo "✅ Build successful!"
    echo "📁 Files generated in dist/:"
    ls -la dist/
    echo ""
    echo "🌐 To test locally:"
    echo "   cd dist && python -m http.server 8000"
    echo "   Then open: http://localhost:8000"
else
    echo "❌ Build failed!"
    exit 1
fi
