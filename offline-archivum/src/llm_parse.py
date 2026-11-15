"""LLM-kutatás YAML-jainak robusztus beolvasása (a flow-mappingekben lévő ':'-ok miatt)."""
import re, yaml
FK = r"(format|repo_url|quant|size|size_status|runtime|tier|tag|notes|files|bytes|url|name|repo|platforms|install)"
def fix_flow(line):
    m = re.match(r"^(\s*-\s*)\{(.*)\}\s*$", line)
    if not m: return line
    body = m.group(2)
    pos = [(mm.start(), mm.group(1)) for mm in re.finditer(r"(?:^|,\s*)" + FK + r":\s", body)]
    if not pos: return line
    out = []
    for i, (p, k) in enumerate(pos):
        start = body.index(k + ":", p) + len(k) + 1
        end = pos[i + 1][0] if i + 1 < len(pos) else len(body)
        v = body[start:end].strip().rstrip(",").strip()
        if v.startswith('"') and v.endswith('"'): v = v[1:-1]
        out.append(f'{k}: "' + v.replace("\\", "\\\\").replace('"', '\\"') + '"')
    return m.group(1) + "{" + ", ".join(out) + "}"
def load_blocks(path):
    t = open(path, encoding="utf-8").read()
    res = []
    for b in re.findall(r"```yaml\n(.*?)```", t, re.S):
        fixed = "\n".join(fix_flow(l) for l in b.splitlines())
        try:
            d = yaml.safe_load(fixed)
        except yaml.YAMLError as e:
            # elemenként
            d = []
            for ch in re.split(r"(?m)^(?=- id:)", fixed):
                if ch.lstrip().startswith("- id:"):
                    try: d += yaml.safe_load(ch) or []
                    except yaml.YAMLError:
                        from convert_research import sanitize
                        try: d += yaml.safe_load(sanitize(ch)) or []
                        except yaml.YAMLError as e2: print("SKIP", ch[:50].strip(), "|", str(e2).splitlines()[0])
        res.append(d)
    return res
