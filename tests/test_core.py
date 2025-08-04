import os
import pytest
from core.ela_analysis import analyze_ela
from core.exif_reader import extract_exif_metadata
from core.hash_utils import generate_image_hashes

TEST_IMAGE = "assets/logo.png"  # Küçük örnek görsel

def test_ela_analysis():
    result = analyze_ela(TEST_IMAGE)
    assert isinstance(result, dict)
    assert "ela_score" in result

def test_exif_reader():
    exif_data = extract_exif_metadata(TEST_IMAGE)
    assert isinstance(exif_data, dict)

def test_hash_generation():
    hashes = generate_image_hashes(TEST_IMAGE)
    assert isinstance(hashes, dict)
    assert "ahash" in hashes
