class HarnessError(Exception):
    """Base harness exception."""


class SchemaError(HarnessError):
    """Input structure or vocabulary is invalid."""


class UnknownKernelError(HarnessError):
    """Kernel profile/version cannot be authoritatively evaluated."""


class PolicyRecheckError(HarnessError):
    """Mandatory final deterministic policy recheck failed."""
