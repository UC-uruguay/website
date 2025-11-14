<?php

			$session_id  = htmlspecialchars( session_id(), ENT_QUOTES, 'UTF-8' );
			$this->token = sha1( $session_id );