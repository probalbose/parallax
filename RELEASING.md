# Releasing Parallax

Parallax uses Semantic Versioning. Before 1.0, a minor version may introduce a
breaking experiment contract; patch releases are backward-compatible fixes.

## Release checklist

1. Ensure CI is green on `main` and the changelog has an `Unreleased` section.
2. Move the relevant entries into a dated `X.Y.Z` section in `CHANGELOG.md`.
3. Commit the release preparation.
4. Create and sign an annotated tag: `git tag -s vX.Y.Z -m "Parallax vX.Y.Z"`.
5. Push the commit and tag: `git push origin main --follow-tags`.
6. Confirm the release workflow publishes the GitHub release and generated notes.
7. Start a fresh `Unreleased` section.

Never move, delete, or reuse a published release tag. If a release is broken,
publish a corrective patch version.

## Change categories

Use Keep a Changelog categories: Added, Changed, Deprecated, Removed, Fixed,
and Security. Link public pull requests and issues where they help users trace a
change.
