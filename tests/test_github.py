from services.github_service import github_service

diff = github_service.get_pr_diff(
    "SomanathBijjargi",
    "github-review-agent-test",
    1
)

print(diff[:2000])