#!/usr/bin/env python3
"""
Gerador de license.key — Minerador 4.0 / Ouro 4.0
Uso interno pela Cara-Core Informática. Não distribuir com o aplicativo.

Uso:
  python gerar_license.py <HARDWARE_ID> [VALID_UNTIL]
  VALID_UNTIL no formato YYYY-MM-DD (padrão: 2099-12-31)

A chave secreta é lida da variável de ambiente LICENSE_SECRET ou
CARA_CORE_LICENSE_SECRET. Se não definida, usa o valor de demonstração
compatível com o painel web (licencas_ete.html).
"""
import hmac
import hashlib
import os
import sys
from pathlib import Path
from typing import Optional

# Mesmo segredo do painel web (licencas_ete.html) para compatibilidade.
# Em produção: definir LICENSE_SECRET no ambiente com valor forte e único.
_SECRET_DEFAULT = b"cara-core-licenca-ouro40-demo"


def _get_secret() -> bytes:
    raw = os.environ.get("LICENSE_SECRET") or os.environ.get("CARA_CORE_LICENSE_SECRET")
    if raw:
        return raw.encode("utf-8") if isinstance(raw, str) else raw
    return _SECRET_DEFAULT


def _sign(secret: bytes, payload: str) -> str:
    return hmac.new(secret, payload.encode("utf-8"), hashlib.sha256).hexdigest()[:32]


def gerar(hardware_id: str, valid_until: str = "2099-12-31", secret: Optional[bytes] = None) -> str:
    hid = hardware_id.strip().upper()
    payload = f"HARDWARE_ID={hid}|VALID_UNTIL={valid_until}"
    sig = _sign(secret or _get_secret(), payload)
    return f"{payload}|SIGNATURE={sig}"


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python gerar_license.py <HARDWARE_ID> [VALID_UNTIL YYYY-MM-DD]", file=sys.stderr)
        sys.exit(1)
    hid = sys.argv[1].strip().upper()
    valid_until = sys.argv[2] if len(sys.argv) > 2 else "2099-12-31"
    secret = _get_secret()
    license_content = gerar(hid, valid_until, secret)
    out_name = f"license_{hid[:12]}.key"
    out_path = Path(out_name)
    out_path.write_text(license_content, encoding="utf-8")
    print(f"Gerado: {out_path}")
    print("Conteúdo (para enviar ao cliente):")
    print(license_content)
    if secret == _SECRET_DEFAULT:
        print("(Segredo de demonstração em uso. Para produção, defina LICENSE_SECRET.)", file=sys.stderr)


if __name__ == "__main__":
    main()
