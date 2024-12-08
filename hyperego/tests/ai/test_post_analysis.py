import logging
from hyperego.ai import PostAnalyzer

from hyperego.scrapers import ScrapeResult

Logger = logging.getLogger(__name__)

def test_analyze_text():
    return
    post = ScrapeResult(
        source="facebook",
        url="https://www.facebook.com/12345/posts/67890",
        title="Birthday Wishes",
        content="Happy birthday to my best friend! I hope you have a great day, Becky!",
    )

    analyzer = PostAnalyzer()
    result = analyzer.analyze(post)

    possible_verdicts = ["professional", "neutral", "unprofessional"]
    assert result.verdict in possible_verdicts, f"Expected verdict to be one of {possible_verdicts}, got {result.verdict}"
    assert 1 <= result.quality <= 10, f"Expected quality to be between 1 and 10, got {result.quality}"

    assert result.verdict != "unprofessional", "Expected a professional or neutral verdict, got unprofessional"

def test_analyze_wacky():
    return
    post = ScrapeResult(
        source="instagram",
        url="https://www.instagram.com/p/12345",
        title="Girls Night Out",
        content="0mg we got so waaasteeeeeeeeeeeeed last night! #girlsnightout #party #drunkashell"
    )

    analyzer = PostAnalyzer()
    result = analyzer.analyze(post)

    possible_verdicts = ["professional", "neutral", "unprofessional"]
    assert result.verdict in possible_verdicts, f"Expected verdict to be one of {possible_verdicts}, got {result.verdict}"
    assert 1 <= result.quality <= 6, f"Expected quality to be between 1 and 6, got {result.quality}"

    assert result.verdict == "unprofessional", "Expected an unprofessional verdict, got professional or neutral"
