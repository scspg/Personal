#!/usr/bin/env bash
# ALGOTRADING – ingyenes források letöltése. Használat: DEST=/abszolut/ut bash letolto.sh
set -u
DEST=${DEST:-}
case "$DEST" in /*) ;; *) echo "DEST abszolút út kell (pl. DEST=/mnt/algo)" >&2; exit 2;; esac
DEST=$(realpath -m -- "$DEST")
case "$DEST" in /|/bin|/boot|/dev|/etc|/home|/lib*|/proc|/root|/run|/sbin|/sys|/usr|/var|/private|/System) echo "Tiltott DEST: $DEST" >&2; exit 2;; esac
mkdir -p "$DEST" && LOG="$DEST/_letoltes.log"
ok(){ echo "OK   $1" | tee -a "$LOG"; }; fail(){ echo "FAIL $1" | tee -a "$LOG"; }


echo "Kész. Napló: $LOG"
