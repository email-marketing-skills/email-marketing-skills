# Evidence to collect

Use redacted headers retaining authentication results, sender domain, return-path domain, DKIM signing domain, timestamps, and relevant recipient-server status. Keep personal addresses and message contents private unless needed and authorized.

Record provider event ID, campaign ID, event type, timestamp, reason code, and retry state. Deduplicate callbacks. Distinguish hard bounces from transient failures using the provider's documented classification. Check an opt-out that arrives while a send is queued.

Primary references to recheck at use time:
- [Gmail sender guidelines](https://support.google.com/mail/answer/81126?hl=en)
- [Yahoo sender best practices](https://senders.yahooinc.com/best-practices/)
- The selected provider's official domain-authentication, webhook, suppression, and acceptable-use documentation.

These are operational references. For jurisdiction-specific rules, consult current authoritative guidance rather than treating deliverability advice as legal advice.
