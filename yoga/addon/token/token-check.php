<?php

		if ( ! ( isset( $_POST['token'] ) && $_POST['token'] === $this->token ) ) {
			echo 'spam_failed-0004,不正な操作が行われたようです。';
			exit;
		}
