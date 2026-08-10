from .provider import DisabledEvidenceProvider


class DisabledGitHubAdapter:
    enabled = False

    def __getattr__(self, name: str):
        raise RuntimeError("GitHub adapter is disabled in the initial offline V0 slice")


__all__ = ["DisabledEvidenceProvider", "DisabledGitHubAdapter"]
