def test_trace(logged_in_page):

    context = logged_in_page.context

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    try:
        logged_in_page.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        ).click()

    finally:
        context.tracing.stop(
            path="traces/test_trace.zip"
        )